<template>
    <div class="mesh-viewer-container">
        <div class="left-container">
            <div class="top-container">
                <div class="mesh-container">
                    <div class='mesh-item'
                        v-for="(item, index) in meshData"
                        :key="index"
                        :id="item.id"
                        @click="setvalue(index)"
                    >
                        <div class="mesh-item-title">{{item.sim_title}}</div>
                        <div class="mesh-cover"></div>
                        <img :src="getImg(item.src)" alt="">
                    </div>
                </div>
                <div class="title-container">
                    <h1>{{ data.title }}</h1>
                    <p>{{ data.dpt }}</p>
                    <analyzeChart/>    
                    <!-- <div class="canvas-container">
                        <canvasItem></canvasItem>
                    </div> -->
                </div>
            </div>
            <div class="progress-container">
                <Timeline>
                </Timeline>
            </div>
        </div>
        <div class="img-window">
            <l-map
                v-model:zoom="zoom"
                v-model:center="data.center"
                style="height: 700px; width: 100%"
                :minZoom="minZoom"
                :maxZoom="maxZoom"
                :maxBounds="maxBounds"
            >
                <l-rectangle
                    v-for="item in meshData"
                    :bounds="item.bounds"
                    :l-style="rectangle.style"
                    :fill = "rectangle.fill"
                    :fillColor="rectangle.fillColor"
                    :opacity = "rectangle.opacity"
                    :color = "rectangle.color"
                    :visible = "layers.visible"
                />
                <l-image-overlay
                    v-for="item in meshData"
                    :url='overlayImg(item.src)'
                    :bounds="item.bounds"
                >
                </l-image-overlay>
                <l-tile-layer
                    :url="url"
                    :attribution="attribution"
                    :options="layerOptions"
                    :tile-layer-class="tileLayerClass"
                />
                
            </l-map>
        </div>
    </div>
    
</template>

<script>
import meshData from '../data/mesh.js'
import { ref, onMounted, watch, computed } from 'vue';
import { L, latLng } from "leaflet";
import {
  LMap,
  LTileLayer,
  LRectangle,
  LWmsTileLayer,
  LImageOverlay
} from "@vue-leaflet/vue-leaflet";

import mapboxgl from 'mapbox-gl'
import 'mapbox-gl-leaflet'
import 'mapbox-gl/dist/mapbox-gl.css'

import canvasItem from './PtsDemo.vue';

import Timeline from './TimeLine.vue';
import analyzeChart from './AnalyzeChart.vue';

window.mapboxgl = mapboxgl // mapbox-gl-leaflet expects this to be global
window.demoDescription = "Demo in getting started guide.";

export default {
    components: {
        LMap,
        LTileLayer,
        LRectangle,
        "l-wms-tile-layer": LWmsTileLayer,
        LImageOverlay,
        canvasItem,
        Timeline,
        analyzeChart
    },
    data(){
        return {
            meshData,
            zoom: 16,
            minZoom: 13,
            maxZoom: 16,
            maxBounds: [
                [30.1780,120.0311],
                [30.4030,120.2700],
            ],
            baseUrl: 'http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi',
            layers: [
                {
                name: 'Weather Data',
                visible: true,
                format: 'image/png',
                layers: 'nexrad-n0r-900913',
                transparent: true,
                attribution: "Weather data © 2012 IEM Nexrad"
                }
            ],
            rectangle: {
                bounds: [[47.341456, -1.397133], [47.303901, -1.243813]],
                color: '#000000',
                fill: true,
                opacity: 0,
                fillColor: 'white',

            },
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attribution:
                '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            tileLayerClass: (url, options) => L.mapboxGL(options),
            layerOptions: {
                accessToken: 'pk.eyJ1IjoicGlub3dpbmUiLCJhIjoiY2xsY2tuNzZ4MDI2djNqcDRya2hvbnE2MiJ9.i2bUXtq9KP1MOrkuBBzZ7A',
                style: 'mapbox://styles/pinowine/clo2txs7j006n01rf59kw8kfn'
            },
            groups: [
                {
                    id: 'seasons',
                    content: 'Seasons',
                    className: 'seasons'

                },
                {
                    id: 'progress',
                    content: 'Progress',
                    className: 'progress'
                }
            ],
            items: [
                {
                    id: 'season1',
                    start: 1640972182172,
                    end: 1698088484172,
                    type: 'range',
                    group: 'seasons',
                },
                {
                    id: 'season2',
                    start: 1540972182172,
                    end: 1598088484172,
                    type: 'range',
                    group: 'seasons',
                },
            ]
            
        };
    },
    setup() {
        const data = ref({
            "id": 1,
            "title": "Unsolved",
            "dpt": "This area will be discovered in the coming series.",
            "src": "1",
            "center": [
                30.2621,
                120.1106
            ],
            "bounds": [
                [
                    30.2571,
                    120.1049
                ],
                [
                    30.267100000000003,
                    120.1163
                ]
            ]
        })


        function setvalue (id) {
            data.value =  meshData[id]
        }

        function overlayImg (src, solved) {
            let randomNum = solved ? 5 : Math.floor(Math.random() * 4) + 1;
            return new URL(`../assets/img/map_images_${randomNum}/map_image_${src}.png`, import.meta.url).href
        }

        const getImg = (path) => {
            return new URL(`../assets/img/mesh/${path}`, import.meta.url).href;
        }

        return {
            getImg,
            setvalue,
            overlayImg,
            data
        }
    }
}

</script>

<style lang="scss" scoped>

.mesh-viewer-container {
    display: flex;
    padding-top:50px;

    .left-container {
        
        .top-container{
            padding-top: 30px;
            display: flex;

            .mesh-container {
                margin-left: 10px;
                width: 280px;
                height: 300px;
                display: flex;
                flex-shrink: 0;
                flex-wrap: wrap;
                flex-direction: column-reverse;
                justify-content: center;
                align-items: center;
                vertical-align: middle;

                .mesh-item {
                    background-color: #745452;
                    box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.1);
                    border-radius: 5px;
                    width: 40px;
                    height: 40px;
                    margin-bottom: 4px;
                    margin-right: 4px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    vertical-align: middle;
                }

                .mesh-item-title {
                    font-size: 20px;
                    z-index : 100;
                    position: absolute;
                    opacity: 0;
                    transition: all 0.3s ease-in-out;
                }

                .mesh-item:hover .mesh-item-title{
                    opacity: 1;
                    transition: all 0.3s ease-in-out;
                }
            }

            .title-container {
                margin-left: 10px;
                h1 {
                    margin-top: 25px;
                    margin-bottom: 40px;
                }
                p {
                    width: 70%;
                }

                .canvas-container {
                    position: absolute;
                    left: 0;
                    top: 0;
                    bottom: 0;
                    right: 0;
                    width: 100%;
                    height: 100%;
                    z-index: -100;
                }
            }

        }

    }

    .img-window {
        width: 60%;
        margin-top: 30px;
    }
}


    
</style>