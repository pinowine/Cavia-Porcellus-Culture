<template>
<div class="car-preview">
    <div
      class="preview-item"
      v-for="item in itemLeng"
      :key="item"
    >
        <a 
            href="javascript:;"
            class="preview-link"
            @click="previewClick(item - 1)"
        >
            <div 
              class="mask"
            ></div>
            <img 
              :src="imgSrc[item - 1]" 
              alt=""
              :style="{opacity: (item - 1) === currentIndex ? maskColor : '1'}"
            >
        </a>
    </div>
</div>
</template>

<script>

export default {
  name: 'CarPreview',
  props: {
    itemLeng: Number,
    currentIndex : Number,
    imgSrc : Array,
    maskColor : {
        type: String,
        default: '0.3'
    }
  },
  setup (props, ctx) {
    const previewClick = (index) => {
        ctx.emit('previewClick', index);
    }

    return {
        previewClick
    }
  }
}
</script>

<style lang="scss" scoped>
.car-preview {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    .preview-item {
        height: 95px;
        width: 200px;
        overflow: hidden;
        a {

            .mask {
                position: absolute;
                width: 200px;
                height: 95px;
                z-index: 100;
                pointer-events: none;
                transition: all 0.2s ease;
            }

            &:hover .mask {
                opacity: 0.4;
                background-color: black;
                transition: all 0.2s ease;
            }

            &:hover img {
                scale: 1.05;
                transition: all 0.4s ease;
            }

            img {
                z-index: 1;
                width: 100%;
                transition: all 0.2s ease;
            }
        }

    }
}

</style>