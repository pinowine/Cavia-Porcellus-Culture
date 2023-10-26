<template>
    <perfect-scrollbar>
            <slot name="sliderItem"></slot>

    </perfect-scrollbar>
</template>

<script>

import { 
    reactive, 
    toRefs,
    onMounted,
    onBeforeUnmount, 
    getCurrentInstance
} from 'vue'

export default {
    name: "Slider",
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
            state.itemLeng = instance.slots.sliderItem()[0].children.length;
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

.ps {
    width: 100%;
    display: flex;
    position: relative;
    height: 500px;
    overflow-y: hidden;
}
    

</style>