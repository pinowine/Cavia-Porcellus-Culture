<template>
<div class="container">
  <div class="map-title">
    <div class="titlecontainer">
        <div class="caps">
            <p class="caps">W</p>
        </div>
        <div class="detailsinfo">
            <p class="slogan"> EMERGENCY: FIND THE MISSING MAN.</p>
            <p class="bigtitle">ELCOME to CPC's workflow <br/> Use this map to start your work.</p>
        </div>
    </div> 
    <div class="canvas-container">
        <ptsDemo />
    </div>
 </div>
  <div class="map-container">
    <div class="l-map-container">
        <l-map 
        :useGlobalLeaflet="false" 
        ref="map" 
        :zoom="zoom" 
        v-model:center="center"
        :options="mapOptions"
        >
            <l-tile-layer 
                :url="url"
                :attribution="attribution"
            ></l-tile-layer>
            <l-marker
                v-if="tooltip.value"
                v-for="marker in markers"
                :key="marker.id"
                :visible="marker.visible"
                :draggable="marker.draggable"
                v-model:lat-lng.sync="marker.position"
                :icon="marker.icon"
                @click="alert(marker)"
            >
                <l-popup :content="marker.tooltip" />
                <l-tooltip :content="marker.tooltip" />
            </l-marker>
        <l-geo-json 
            v-if="POI.value"
            :geojson="geojson" 
            :options="geojsonOptions" 
            :options-style="styleFunction"
        />
        </l-map>
    </div>
    <div class="addon">
        <h3>List of Markers</h3>
        <button
            name="button"
            @click="addMarker"
        >
            Add a marker
        </button>
        <table class="head">
            <tr>
                <th class="Marker" >Marker</th>
                <th class="Lat" style="padding-left: 10px;">Latitude</th>
                <th class="Lng">Longitude</th>
                <th class="Tooltip">Tooltip</th>
                <th class="Draggable">Allow<br/>Drag</th>
                <th class="Visible" style="padding-left: 10px;">Visible<br/>or not</th>
                <th class="Remove" style="padding-left: 10px;">Remove<br/>Mark</th>
            </tr>
            <tr
                style="line-height: 1px;visibility: hidden;font-size: 1px;height: 1px;overflow: hidden;"
            >
                <td>Mark0</td>
                <td>
                    <input
                    type="number"
                    >
                </td>
                <td>
                    <input
                    type="number"
                    >
                </td>
                <td>
                    <input
                    type="text"
                    >
                </td>
                <td style="text-align: center">
                    <input
                    type="checkbox"
                    >
                </td>
                <td style="text-align: center">
                    <input
                    type="checkbox"
                    >
                </td>
                <td style="text-align: center">
                    <input
                    type="button"
                    value="X"
                    >
                </td>
            </tr>
        </table>
        <hr>
        <table class="content">
            <perfect-scrollbar>
                <tr style="visibility: hidden;font-size: 1px;line-height: 0;">
                    <th>Marker</th>
                    <th>Lat</th>
                    <th>Lng</th>
                    <th>Tooltip</th>
                    <th>Draggable</th>
                    <th>Visible</th>
                    <th>Remove</th>
                </tr>
                <tr
                v-for="(item, index) in markers"
                :key="index"
                >
                    <td>{{ 'Mark' + (index + 1)}}</td>
                    <td>
                        <input
                        v-model.number="item.position.lat"
                        type="number"
                        >
                    </td>
                    <td>
                        <input
                        v-model.number="item.position.lng"
                        type="number"
                        >
                    </td>
                    <td>
                        <input
                        v-model="item.tooltip"
                        type="text"
                        >
                    </td>
                    <td style="text-align: center">
                        <input
                        v-model="item.draggable"
                        type="checkbox"
                        >
                    </td>
                    <td style="text-align: center">
                        <input
                        v-model="item.visible"
                        type="checkbox"
                        >
                    </td>
                    <td style="text-align: center">
                        <input
                        type="button"
                        value="X"
                        @click="removeMarker(index)"
                        >
                    </td>
                </tr>
            </perfect-scrollbar>
        </table>
        <hr>
        
        <div class="tooltip">
            <span>Show Marks</span>
            <Toggle
            v-model="tooltip.value"
            v-bind="tooltip"
            @click="tooltip.value = !tooltip.value"
            >
                <template v-slot:label="{ checked, classList }">
                    <span :class="classList.label">{{ checked ? 'On' : 'Off' }}</span>
                </template>
            </Toggle>
        </div>

        <hr>

        <div class="poi">
            <span>Show POI Data</span>
            <Toggle
            v-model="POI.value"
            v-bind="POI"
            @click="POI.value = !POI.value"
            >
                <template v-slot:label="{ checked, classList }">
                    <span :class="classList.label">{{ checked ? 'On' : 'Off' }}</span>
                </template>
            </Toggle>
        </div>
        <div class="fillColor">
            <span>POI Fill Color Adjust</span>
            <input
                v-model="fillColor"
                type="color"
            >
        </div>
    </div>
  </div>
</div>
</template>

<script>
// DON'T load Leaflet components here!
// Its CSS is needed though, if not imported elsewhere in your application.
import "leaflet/dist/leaflet.css";
import { ref } from "vue";
import {latLng} from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup, LTooltip, LGeoJson } from "@vue-leaflet/vue-leaflet";
import Toggle from "./Toggle.vue";

import ptsDemo from './PtsDemo.vue'


let zoom = ref(6)
let center = ref([38, 139.69])

export default {
  
  components: {
    LMap,
    LGeoJson,
    LTileLayer,
    LMarker,
    LPopup,
    LTooltip,
    Toggle,
    ptsDemo
  },
  data() {
    return {
        addonLat: '',
        addonLng: '',
        zoom: 14,
        center: latLng(30.2677, 120.1320),
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution:
            '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        withTooltip: latLng(47.41422, -1.250482),
        currentZoom: 11.5,
        currentCenter: latLng(30.2677, 120.1320),
        showParagraph: false,
        geojson: null,
        POI: {
            value: true,
        },
        tooltip: {
            value: true,
        },
        fillColor: "#e4ce7f",
        enableTooltip: true,
        mapOptions: {
            zoomSnap: 0.5
        },
        showMap: true,
        heatmapLayer: null,
        geojsonOptions : {
            radius: 20,
            fillColor: "#ff7800",
            color: "#000",
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8,
        },
        markers: [ 
            {
                id: 'm1',
                position: {lat: 30.218437, lng: 120.129702},
                tooltip: '杭州少年儿童公园',
                draggable: true,
                visible: true,
            }
        ]
    };
  },
  methods: {
    addlocation(lat,lng) {
      return latLng(lat,lng)
    },
    alert(item) {
      alert('this is ' + JSON.stringify(item));
    },
    addMarker: function() {
      const newMarker = {
        position: { lat: 30.218437, lng: 120.129702 },
        draggable: true,
        visible: true,
      };
      this.markers.push(newMarker);
    },
    removeMarker: function(index) {
      this.markers.splice(index, 1);
    },
  },
  computed: {
    styleFunction() {
      const fillColor = this.fillColor; // important! need touch fillColor in computed for re-calculate when change fillColor
      return () => {
        return {
          weight: 2,
          color: "#ECEFF1",
          opacity: 1,
          fillColor: fillColor,
          fillOpacity: 1
        };
      };
    },
  },
  async created() {
    this.loading = true;
    const response = await fetch("src/data/merged_data.json")
    const data = await response.json();
    this.geojson = data;
    this.loading = false;
  },
  async beforeMount() {
    // HERE is where to load Leaflet components!
    const { circleMarker } = await import("leaflet/dist/leaflet-src.esm");

    // And now the Leaflet circleMarker function can be used by the options:
    this.geojsonOptions.pointToLayer = (feature, latLng) =>
      circleMarker(latLng, { radius: 8 });
    this.geojsonOptions.onEachFeature = (feature, layer) => {
        if (!this.enableTooltip) {
          return () => {};
        }
        layer.bindTooltip(
          "<div>name:" +
            feature.properties.name +
            "</div><div>amenity: " +
            feature.properties.amenity +
            "</div>",
          { permanent: false, sticky: true }
        );
    };
    this.mapIsReady = true;
  },
};
</script>

<style lang="scss" scoped>
.container {
    padding-left: 20px;
    padding-top: 60px;
    
    .map-title {
        .canvas-container {
            position: absolute;
            left: 0;
            top: 0;
            display: flex;
            z-index: -999;
            height: 20rem;
            width: 100%;
            overflow-x: visible;
        }

        .titlecontainer {
            display: flex;
            margin-top: 50px;
            border-bottom: 4px solid #000;
            .caps {
                font : {
                    size:150px;
                    weight:bolder;               
                }
                line-height: 90.582%; /* 212.868px */
            }
            .detailsinfo {
                padding-top:10px;

                .slogan {
                    font-size: 20px;
                    text-decoration: underline;
                }

                .bigtitle {
                    margin-top: 44px;
                    font : {
                        size:30px;
                        weight:bold;
                    }
                    line-height: 90.582%; /* 57.972px */
                }
            }
        }
    }
    

    

    .map-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-right: 30px;

        .l-map-container {
            height: 600px;
            width: 60%;
        }

        .addon {
            width: 40%;
            border-radius: 5px;
            border: 2px solid #000000;
            background-color: #F4F4F4;
            box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
            padding: 10px;
            padding-top: 15px;
            margin-top: 10px;
            margin-left: 10px;

            .add-mark {
                border-bottom: 2px solid #ababab;
            }

            label {
                font-size: 10px;
                font-weight: bold;
                color: #272727;
            }

            input {
                padding-left: 5px;
                padding-right: 5px;
                margin-bottom: 5px;
                font-size: 15px;
                font-weight: lighter;
                color: #AAA;
                margin-top: 10px;
                width: 70%;
                height: 20px;
                border-radius: 6px;
                border: 1px solid #AAA;
                background: #FFF;
                font-size: 10px;

                &[type = 'checkbox'] {
                    color: #ababab;
                }
            }

            table.head {

                border-collapse: collapse;
                display: block;
                max-height: 36px;
                width: 100%;
                overflow-y: hidden;

                th {
                    font-size: 11px;
                    text-align: start;
                }

                td {
                    font-size: 10px;
                }

            }
            table.content {
                border-collapse: collapse;
                margin: 1rem 0;
                height: 200px;
                display: block;
                overflow-y: auto;
                width: 100%;

                th {
                    font-size: 10px;
                    text-align: start;
                }

                td {
                    font-size: 10px;
                }
            }

            .tooltip, .poi, .fillColor {
                display: flex;
                flex-direction: row;
                justify-content: space-between;
                vertical-align: middle;
                flex-shrink: 1;
                flex-grow: 0;
                margin-top: 10px;
                margin-bottom: 10px;

                span {
                    padding-top: 5px;
                    font-weight: bold;
                }

                input {
                    width: 50%;
                    height: 40px;
                }

            }
        }

    }

}

button {
    font-weight: bold;
    width: 20%;
    margin-top: 20px;
    margin-bottom: 20px;
    border-radius: 6px;
    border: 1px solid #AAA;
    background: #FFF;
    box-shadow: 1px 0px 4px 0px rgba(0, 0, 0, 0.25);
    padding-top: 5px;
    padding-bottom: 5px;
    transition: all 0.3s ease-in-out;

    &:hover {
        background-color: #d4d4d4;
        transition: all 0.3s ease-in-out;
    }
}

</style>