<template>
    <transition>
        <div class="slider-item">
            <div class="mask"></div>
            <slot></slot>
        </div>
    </transition>
</template>

<script>

import { 
    getCurrentInstance, 
    reactive, 
    toRefs,
    watch
} from 'vue';

export default {
    name : "SliderItem",
    setup(){
        const instance = getCurrentInstance();

        const state = reactive({
            selfIndex: instance.vnode.key,
            curentIndex: instance.parent.ctx.currentIndex
        });

        watch(() => {
            return instance.parent.ctx.currentIndex;
        }, (value) => {
            state.curentIndex = value;
        })

        return {
            ...toRefs(state)
        }
    }
}

</script>

<style lang='scss' scoped>
.slider-item {
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    .mask {
        position: absolute;
        z-index: -10;
        width: 280px;
        height: 100%;
        pointer-events: none;
        background-color: black;
    }

}



.v-enter-active,
.v-leave-active {
    transition: all 0.5s ease-in-out;
}
/* 动画开始之前 */

.v-enter-from {
    transform: translateX(5%);
    opacity: 0;
}

.v-enter-to {
    transform: translateX(0);
    opacity: 1;
}

.v-leave-active {
    transform: translateX(0);
    opacity: 0;
}

.v-leave-to {
    transform: translateX(0);
    opacity: 0;
}

</style>
