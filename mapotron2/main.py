import logging
import os
import json
from flask.helpers import send_from_directory
from markupsafe import escape
import requests
import ee

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import config
import ee_config

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config.update(
    GMAPS_KEY=config.GMAPS_KEY
)


@app.template_filter()
def vue(item):
    # If you see anything about "raw", blame the blog engine, not me. If not,
    # ignore these comments.
    return "{{ " + item + " }}"


def get_image(collection_id, layer_id, coll_year=None):
    if collection_id not in ee_config.collections:
        raise Exception(f'Collection not found: {collection_id} .')

    collection = ee_config.collections[collection_id]
    if layer_id is None:
        show = [k for k in collection['layers']
                if collection['layers'][k]['show']]

        if len(show) > 0:
            layer_id = show[0]
        else:
            layer_id = [k for k in collection['layers']][0]
        
    if layer_id not in collection['layers']:
        raise Exception(f'Layer not found: {layer_id} .')

    layer = collection['layers'][layer_id]

    if layer_id == 'daily_precip_v21':
        prec_start_date = '2016-01-01'
        prec_end_date = '2017-01-01'
        try:
            if coll_year is not None:
                prec_start_date = f"{int(coll_year)}-01-01"
                prec_end_date = f"{int(coll_year) + 1}-01-01"
        except Exception as ex:
            raise Exception(f'Invalid precipitation date.')
        
        imgByYear = ee.ImageCollection('projects/earthenv/chelsa/daily_precip_land_v21').filterDate(prec_start_date, prec_end_date).mean().multiply(0.01)
        return ee.Image(imgByYear), collection, layer

    if collection_id == 'tcf':
        if layer_id == 'tcf_ensemble_mn_v16':
            tcf_start_date = '2018-01-01'
            try:
                if coll_year is not None:
                    tcf_start_date = f"{int(coll_year)}-01-01"
            except Exception as ex:
                raise Exception(f'Invalid TCF date.')
            
            imgByYear = ee.ImageCollection(layer['id']).filterDate(tcf_start_date).first().divide(100)
            return ee.Image(imgByYear), collection, layer
        
        if layer_id == 'tcf_ensemble_mnv16_2001-2018':
            imgVariable = ee.Image(layer['id']).divide(100)
            return ee.Image(imgVariable), collection, layer
        
        if layer_id == 'tcf_wdpa_Dec2016_v16':
            imgOutline = ee.Image(0).mask(0).paint(ee.FeatureCollection(layer['id']), 1, 2)
            return ee.Image(imgOutline), collection, layer

    if collection_id == 'mountains':
        gmba_level_fc = ee.FeatureCollection(layer['id'])
        color_column = 'ColorBasic' if layer_id == 'basic' else 'ColorAll'
        imgOutline = ee.Image(0).mask(0).paint(gmba_level_fc, color_column).paint(gmba_level_fc, color_column, 1)
        
        return ee.Image(imgOutline), collection, layer

    logging.info(f'Generating new map from: {layer["id"]}')

    return ee.Image(layer["id"]), collection, layer


def get_map(collection_id, layer_id, coll_year=None):
    image, collection, layer = get_image(collection_id, layer_id, coll_year)
    # this is where I imagine putting .clip(bbox)...
    geodesic = ee.Geometry.Rectangle(-180, -85, 180, 85)
    bbox = ee.Geometry(geodesic, None, False)

    if layer_id != 'tcf_ensemble_mnv16_2001-2018':
        image = image.mask(image.gt(0))
    
    mapid = image.getMapId(layer["viz_params"])
    
    return {
        'map': {
            'mapid': mapid['mapid'],
            'token': mapid['token']
        },
        'layer': layer,
        'collection': collection,
        'collection_id': collection_id,
        'layer_id': layer['layer_id'],
    }


@app.route('/config')
def hello():
    """Return a friendly HTTP greeting."""
    return jsonify(ee_config.collections)


@app.route('/map/<collection_id>/<layer_id>')
def map(collection_id, layer_id):
    """Return a friendly HTTP greeting."""

    coll_year = request.args.get("year", None)
    
    if collection_id == 'precipitation' and coll_year is None:
        coll_year = 2016
    if collection_id == 'tcf' and coll_year is None:
        coll_year = 2018
    
    map_info = get_map(collection_id, layer_id, coll_year=coll_year)
    map_info['collection'] = None
    return jsonify(map_info)


@app.route('/page/<collection_id>/<layer_id>')
def page(collection_id, layer_id):
    """Return a friendly HTTP greeting."""
    map_info = get_map(collection_id, layer_id)
    return render_template('page.html', **map_info)


@app.route('/<collection_id>')
def vue(collection_id):
    """Return a friendly HTTP greeting."""
    coll_year = request.args.get("year", None)
    
    if collection_id == 'precipitation' and coll_year is None:
        coll_year = 2016
    if collection_id == 'tcf' and coll_year is None:
        coll_year = 2018
    
    map_info = get_map(collection_id, None, coll_year=coll_year)
    
    if collection_id == 'precipitation':
        return render_template('precipitation.html', **map_info)
    
    if collection_id == 'tcf':
        return render_template('tcf.html', **map_info)
    
    # if collection_id == 'mountains':
    #     return render_template('mountains.html', **map_info)
    
    return render_template('vue.html', **map_info)


@app.route('/sample/<collection_id>/<x>/<y>')
def sample(collection_id, x, y):
    """Return a friendly HTTP greeting."""

    x = float(x)
    y = float(y)
    if collection_id not in ee_config.collections:
        raise Exception(f'Collection not found: {collection_id} .')

    collection = ee_config.collections[collection_id]

    images = []

    result = None

    if collection_id == 'precipitation':
        coll_year = request.args.get("year", 2016)

        prec_start_date = '2016-01-01'
        prec_end_date = '2016-01-01'
        try:
            if coll_year is not None:
                prec_start_date = f"{int(coll_year)}-01-01"
                prec_end_date = f"{int(coll_year) + 1}-01-01"
        except Exception as ex:
            raise Exception(f'Invalid precipitation date.')
        imgColByYear = ee.ImageCollection('projects/earthenv/chelsa/daily_precip_land_v21').filterDate(prec_start_date, prec_end_date)
        
        hist = ee.FeatureCollection(imgColByYear.map(lambda i: i.set(i.unmask().reduceRegion(reducer=ee.Reducer.mean(), scale=1000, geometry=ee.Geometry.Point([x, y]), maxPixels=1e8).rename(['b1'],['mean'])))).sort('system:time_start')
        hist = ee.Dictionary({"histogram": hist.aggregate_array('mean').join(",")})

        result = ee.Feature(None).setMulti({"name": "CHELSA-EarthEnv Precipitation Rate", "title": "Precipitation Rate", "layer_id": "daily_precip_v21", "units": "kg*m^-2*day^-1", "values": hist}).getInfo()
    elif collection_id == 'tcf_single':
        coll_year = request.args.get("year", 2016)

        tcf_start_date = '2016-01-01'
        try:
            if coll_year is not None:
                tcf_start_date = f"{int(coll_year)}-01-01"
        except Exception as ex:
            raise Exception(f'Invalid precipitation date.')
        for k in collection['layers']:
            v = collection['layers'][k]
            imgByYear = ee.ImageCollection(v['id']).filterDate(tcf_start_date).first().divide(100)
            images.append(imgByYear.set(v).set("name", k).set("image", k))

        result = ee.ImageCollection(images).map(
            lambda i:
                ee.Feature(None).copyProperties(i).set(
                    "values", i.reduceRegion(
                        reducer=ee.Reducer.first(),
                        geometry=ee.Geometry.Point([x, y])))
        ).getInfo()
    elif collection_id == 'tcf':
        result = {'features': []}
        for k in reversed(collection['layers']):
            v = collection['layers'][k]
            if v["layer_id"] == 'tcf_ensemble_mn_v16':
                imgMnColByYear = ee.ImageCollection('projects/earthenv/tcf/tcf_ensemble_mn_v16')
                hist_mn = ee.FeatureCollection(imgMnColByYear.map(lambda i: i.set(i.divide(100).unmask().reduceRegion(reducer=ee.Reducer.mean(), scale=1000, geometry=ee.Geometry.Point([x, y]), maxPixels=1e8).rename(['b1'],['mean'])))).sort('system:time_start')
                imgSdColByYear = ee.ImageCollection('projects/earthenv/tcf/tcf_ensemble_sd_v16')
                hist_sd = ee.FeatureCollection(imgSdColByYear.map(lambda i: i.set(i.divide(100).unmask().reduceRegion(reducer=ee.Reducer.mean(), scale=1000, geometry=ee.Geometry.Point([x, y]), maxPixels=1e8).rename(['b1'],['mean'])))).sort('system:time_start')
                hist = ee.Dictionary({"histogram": hist_mn.aggregate_array('mean').join(","), "stdev": hist_sd.aggregate_array('mean').join(",")})
                res = ee.Feature(None).setMulti({"name": "tcf_ensemble_mn_v16", "title": "Percent of area covered", "layer_id": "tcf_ensemble_mn_v16", "units": "percent area covered", "values": hist}).getInfo()
                result['features'].append(res)
            elif v["layer_id"] == 'tcf_ensemble_mnv16_2001-2018':
                images.append(ee.Image(v["id"]).set(v).set("name", k).set("image", k))
                res = ee.ImageCollection(images).map(
                    lambda i:
                        ee.Feature(None).copyProperties(i).set(
                            "values", i.reduceRegion(
                                reducer=ee.Reducer.first(),
                                geometry=ee.Geometry.Point([x, y])))
                ).getInfo()
                result['features'].append(res['features'][0])
            elif v["layer_id"] == 'tcf_wdpa_Dec2016_v16':
                tcf_fc = ee.FeatureCollection(v['id']).filterBounds(ee.Geometry.Point([x, y]))
                res = tcf_fc.getInfo()
                if "features" in res:
                    for f in res['features']:
                        tcfensmn01 = f['properties']['tcfensmn01'] / 10000
                        tcfensmn18 = f['properties']['tcfensmn18'] / 10000
                        tcfensmnvar = tcfensmn01 - tcfensmn18
                        tcfensmnpct = (tcfensmnvar/tcfensmn01) * 100
                        result['features'].append({
                            "type": "Feature",
                            "geometry": None,
                            "id": "0",
                            "properties": {
                                "id": v["id"],
                                "layer_id": v["layer_id"],
                                "name": v["layer_id"],
                                "show": v["show"],
                                "title": v["title"],
                                "values": {
                                    'NAME': f['properties']['NAME'],
                                    'ISO3': f['properties']['ISO3'],
                                    'IUCN_CAT': f['properties']['IUCN_CAT'],
                                    'STATUS': f['properties']['STATUS'],
                                    'STATUS_YR': f['properties']['STATUS_YR'],
                                    'WDPAID': f['properties']['WDPAID'],
                                    'tcfensmn01': f"{tcfensmn01:.4f}",
                                    'tcfensmn18': f"{tcfensmn18:.4f}",
                                    'tcfensmnvar': f"{tcfensmnvar:.4f}",
                                    'tcfensmnpct': f"{tcfensmnpct:.2f}%",
                                }
                            },
                        })
    elif collection_id == 'mountains':
        result = {'features': []}
        v = collection['layers']['basic']
        gmba_fc = ee.FeatureCollection('projects/map-of-life/regional/GMBA/v2/inventory_v2_20210916').filterBounds(ee.Geometry.Point([x, y]))
        gmba_fc_nogeom = gmba_fc.map(lambda f: ee.Feature(None).copyProperties(f))
        res = gmba_fc_nogeom.getInfo()
        if "features" in res:
            for f in res['features']:
                result['features'].append({
                    "type": "Feature",
                    "geometry": None,
                    "id": "0",
                    "properties": {
                        "id": v["id"],
                        "layer_id": v["layer_id"],
                        "name": v["layer_id"],
                        "show": v["show"],
                        "title": v["title"],
                        "values": {
                            'MapName': f['properties']['MapName'],
                            'Countries': f['properties']['Countries'],
                            'Path': f['properties']['Path'],
                            'Area': f['properties']['Area'],
                            'Elev_Low': f['properties']['Elev_Low'],
                            'Elev_High': f['properties']['Elev_High'],
                            'WikiDataID': f['properties']['WikiDataID'],
                            'WikiDataURL': f['properties']['WikiDataUR'],
                        }
                    },
                })
    else:
        for k in collection['layers']:
            v = collection['layers'][k]
            logging.info(v)
            if "query_assets" in v:
                for a in v["query_assets"]:
                    images.append(ee.Image(a["id"]).set(a).set(
                        "name", k).set("image", a["name"]))

            else:
                images.append(ee.Image(v["id"]).set(v).set(
                    "name", k).set("image", k))

        result = ee.ImageCollection(images).map(
            lambda i:
                ee.Feature(None).copyProperties(i).set(
                    "values", i.reduceRegion(
                        reducer=ee.Reducer.first(),
                        geometry=ee.Geometry.Point([x, y])))
        ).getInfo()

    response = {}
    if "features" in result:
        for feature in result["features"]:
            try:
                if feature["properties"]["name"] not in response:
                    response[feature["properties"]["name"]] = []
                response[feature["properties"]["name"]].append(
                    feature["properties"])
            except Exception as e:
                logging.info(e)
    else:
        feature = result
        try:
            if feature["properties"]["name"] not in response:
                response[feature["properties"]["name"]] = []
            response[feature["properties"]["name"]].append(
                feature["properties"])
        except Exception as e:
            logging.info(e)

    return jsonify(response)


@app.route('/')
def index():
    """Return a friendly HTTP greeting."""

    return render_template('index.html', **{
        'collections': ee_config.collections
    })


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/_ah/warmup')
def warmup():
    return '', 200, {}


def handle_bad_request(e):
    return f'{e}', 500


app.register_error_handler(500, handle_bad_request)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.config.update(
        GMAPS_KEY=config.GMAPS_DEV_KEY
    )

    app.run(host='127.0.0.1', port=8080, debug=True)
