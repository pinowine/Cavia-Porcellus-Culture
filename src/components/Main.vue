<template>
<div class="main-container">
    <div class="left-container">
        <div class="titlecontainer">
            <div class="caps">
                <p class="caps">A</p>
            </div>
            <div class="detailsinfo">
                <p class="slogan">Contact us for the best design service!</p>
                <p class="bigtitle">UTUMN Collection VOL#1 <br/> in release now</p>
            </div>
        </div>
        <div class="carousel-container">
            <carousel
            :initial = '0'
            :imgSrc = 'imgSrc'
            >
                <template v-slot:carItem>
                    <car-item
                        v-for= "(item, index) of carData"
                        :key = "index"
                    >
                        <router-link :to="'/autumn-collection/'+item.id">
                            <img :src="getImg(item.img_src)" alt="" />
                            <p class="img-name">{{ item.name }}</p>
                            <p class="img-slogan">{{ item.slogan }}</p>
                        </router-link>
                    </car-item>
                </template>                      
            </carousel>
        </div>
    </div>
    <div class="right-container">
        <login />
        <div class="canvas-container"><ptsDemo></ptsDemo></div>
    </div>
</div>
<div class="slider-container">
    <div class="titlecontainer">
        <div class="caps">
            <p class="caps">F</p>
        </div>
        <div class="detailsinfo">
            <p class="slogan">Contact us for the best design service!</p>
            <p class="bigtitle">OMER Series<br/>Free to Review!</p>
        </div>
    </div>
        <slider
        :initial = '0'
        >
            <template v-slot:sliderItem>
                <slider-item
                    v-for= "(item, index) of sliderData"
                    :key = "index"
                >
                    <img :src="getSlider(item.id)" alt=""/>
                    <p class="img-name">{{ item.name }}</p>
                    <p class="img-date">{{ item.date }}</p>
                </slider-item>
            </template>    
        </slider>
</div>
</template>

<script>
import sliderData from '../data/slider';
import carData from '../data/carousel';
import login from './Login';
import ptsDemo from './PtsDemo.vue'

export default {
    name: 'maincontent',

    components: {
        login,
        ptsDemo
    },
    setup () {
        const getImg = (path) => {
            return new URL(`../assets/img/${path}`, import.meta.url).href;
        }

        const getSlider = (id) => {
            return new URL(`../assets/img/Slides/${id}.jpg`,import.meta.url).href;
        }

        const imgSrc = [];
        for (const item of carData) {
            imgSrc.push(getImg(item.img_src));
        }

        return {
            sliderData,
            carData,
            getImg,
            getSlider,
            imgSrc
        }
    }
}
</script>

<style lang="scss" scoped>

.main-container {
    margin-top: 40px;
    padding-left: 60px;
    padding-right: 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
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

.left-container {
    width: 100%;

    .carousel-container {

        margin-top: 50px;

        .car-item {

            img {
                height: 100%;
                z-index: -1;
            }

            &:hover p {
                transform: translateY(-10px);
                transition: all 0.3s ease;
            }

            p {
                animation: {
                    name:slidein;
                    duration:1s;
                };
                position: absolute;
                z-index: 999;
                top: 420px;
                left: 25px;
                color: aliceblue;
                text-shadow: #2121218a 1px 1px 10px;
                transition: all 0.3s ease;

                &.img-name {
                    font: {
                        size:40px;
                        weight:bold;
                    };
                    text-decoration: underline;
                }

                &.img-slogan {
                    top:455px;
                }
            }
        }

    }

    @keyframes slidein {
        from {
            opacity: 0;
            margin-left: 100%;
            width: 300%;
        }

        to {
            opacity: 1;
            margin-left: 0%;
            width: 100%;
        }
    }
}

.right-container {
    margin-right: 4%;

    .canvas-container {
        position: absolute;
        z-index: -999;
        right: 0;
        top:11.5rem;
        height: 40rem;
        overflow-x: hidden;
        display: flex;
        flex-direction: row-reverse;
    }
}

.slider-container {
    margin-top: 80px;
    margin-left: 60px;
    margin-right: 60px;

    &::-webkit-scrollbar-track {
        display: none;
    }

    &::-webkit-scrollbar-thumb {
        background: rgba(0, 0, 0, 0.3);
        transition: all 0.5s ease;
    }

    &::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    .slider-item {
        margin-right: 10px;
        width: 100%;
        transition: all 0.5s ease-in-out;

        img {
            height: 100%;
            transition: all 0.5s ease-in-out;
        }

        p {
            transition: all 0.5s ease-in-out;
        }

        &:hover { 
            img {
                opacity: 50%;
                transition: all 0.5s ease-in-out;
            }
            p.img-name {
                opacity: 100%;
                transform: translateY(-10px);
                transition: all 0.5s ease-in-out;
            }
            p.img-date {
                opacity: 100%;
                transform: translateY(-10px);
                transition: all 0.5s ease-in-out;
            }
        }

        p.img-name {
            opacity: 0;
            font-size: 30px;
            font-weight: bold;
            color: aliceblue;
            position: absolute;
            padding-left: 20px;
            top:430px;
            z-index: 10;
        }

        p.img-date {
            opacity: 0;
            font-size: 20px;
            color: aliceblue;
            position: absolute;
            padding-left: 20px;
            top:455px;
            z-index: 11;
        }
    }


}
</style>