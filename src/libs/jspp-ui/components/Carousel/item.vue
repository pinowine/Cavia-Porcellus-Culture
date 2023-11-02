<template>
    <transition>
        <div class="car-item" v-if="selfIndex === curentIndex">
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
    name : "CarItem",
    setup(){
        const instance = getCurrentInstance();
        console.log(instance)

        const state = reactive({
            selfIndex: instance.vnode.key,
            curentIndex: instance.parent.proxy.currentIndex
        });

        watch(() => {
            return instance.parent.proxy.currentIndex;
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
.car-item {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
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