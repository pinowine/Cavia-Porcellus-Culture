<template>
    <div class="carousel">
        <div class="inner">
            <slot name="carItem"></slot>
        </div>

        <CarPreview
            :itemLeng="itemLeng"
            :currentIndex="currentIndex"
            :maskColor="maskColor"
            :imgSrc="imgSrc"
            @previewClick = "previewClick"
        />
    </div>
</template>

<script>

import { 
    reactive, 
    toRefs,
    onMounted,
    onBeforeUnmount, 
    getCurrentInstance
} from 'vue'

import CarPreview from './preview';

export default {
    name: "Carousel",
    components: {
        CarPreview
    },
    props: {
        initial: {
            type : Number,
            default: 0
        },
        maskColor: String,
        imgSrc: Array,
    },
    setup (props) {
        const instance = getCurrentInstance();

        const state = reactive ({
            currentIndex: props.initial,
            itemLeng: 0,
        });

        const setIndex = (dir) => {
            switch (dir) {
                case 'next':
                    state.currentIndex = state.currentIndex + 1;
                    if (state.currentIndex === state.itemLeng) {
                        state.currentIndex = 0;
                    }
                    break;
                case 'prev':
                    state.currentIndex = state.currentIndex - 1;
                    if (state.currentIndex === -1) {
                        state.currentIndex = state.itemLeng - 1;
                    }
                    break;
                default:
                    break;
            }
        }

        const previewClick = (index) => {
            state.currentIndex = index;
        }

        onMounted(() => {
            // console.log(state.currentIndex);
            state.itemLeng = instance.slots.carItem()[0].children.length;
            // console.log(instance);
        });

        onBeforeUnmount(() => {
            // console.log(state.currentIndex);
        })

        return {
            ...toRefs(state),
            previewClick
        }
    }
}
</script>

<style lang="scss" scoped>
  .carousel {
    height: 100%;
    width: 100%;
    display: flex;
    overflow: hidden;

    .inner {
        position: relative;
        width: 720px;
        height: 500px;
        margin-right: 6px;
    }
  }
</style>