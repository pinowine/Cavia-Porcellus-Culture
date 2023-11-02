<template>
  <div class="selector-menu">
    <template v-if="searchData.length > 0">
      <div 
        class="menu-item"
        v-for="(item, index) of searchData"
        :key="index"
        @click="setItemValue(item)"
      >
        {{ item.text }}
      </div>
    </template>
    <NoDataTip v-else />
  </div>
</template>

<script>

import NoDataTip from './NoDataTip';

import { watch, onMounted, ref } from 'vue';

export default {
  name: 'SelectorMenu',
  components: {
    NoDataTip
  },
  props: {
    searchValue: String,
    data: {
      type: Array,
      default: [
        {
          id: 1,
          value: '1',
          text: '选项1'
        },
        {
          id: 2,
          value: '2',
          text: '选项2'
        },
        {
          id: 3,
          value: '3',
          text: '选项3'
        }
      ]
    }
  },
  setup (props, proxy) {
    const searchData = ref([]);
    const hasTypedFirstLetter = ref(false);

    const setItemValue = (item) => {
      proxy.emit('setItemValue', item);
    }

    onMounted(() => {
      searchData.value = props.data;
    })

    const filterData = (value) => {
      if (value.length>0){
        searchData.value = props.data.filter((item) => {
          return item.text.toLowerCase().includes(props.searchValue.toLowerCase());
        });
      }
    }

    watch(() => {
      return props.searchValue;
    }, (value) => {
      filterData(value);
    })

    return {
      setItemValue,
      searchData
    }
  }
}
</script>

<style lang="scss" scoped>
  .selector-menu {
    display: none;
    position: absolute;
    left: 0;
    top: 70px;
    width: 748px;
    max-height: 232px;
    border: 1px solid #000;
    background: #FFF;
    box-shadow: 2px 1px 6px 1px rgba(0, 0, 0, 0.20);
    overflow: hidden;
    z-index: 0;
    
    .menu-item {
      height: 35px;
      text-align: center;
      line-height: 35px;
      font-size: 18px;
      color: #666;
      margin: 10px 0;
      transition: background-color .2s linear;

      &:hover {
        background-color: #ededed;
      }
    }
  }
</style>