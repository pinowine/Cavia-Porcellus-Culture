<template>
  <div class="selector-input">
    <span class="iconfont icon-search"></span>
    <label class="placeholder">{{ placeholder }}</label>
    <input 
      type="text"
      class="input"
      ref="inputValue"
      :value="value"
      @input="searchOptions($event)"
      @focus="searchOptions($event)"
      @blur="setValue(value)"
    />
  </div>
</template>

<script>

import { ref, getCurrentInstance } from 'vue';

export default {
  name: 'SelectorInput',
  props: {
    placeholder: {
      type: String,
      default: 'Search for your need'
    },
    value: String
  },
  setup (props, proxy) {
    const instance = getCurrentInstance();

    const searchOptions = (e) => {
      proxy.emit('searchOptions', e.target.value);
    }

    const setValue = (value) => {
      const _input = instance.refs.inputValue;
      if (_input.value.length > 0) {
        _input.value = value;
      }
    }

    return {
      searchOptions,
      setValue
    }
  }
}
</script>

<style lang="scss" scoped>
  .selector-input {
    position: relative;
    width: 750px;
    height: 40px;
    z-index: 10;

    .input {
      width: 100%;
      height: 100%;
      padding: 0 15px;
      padding-left: 80px;
      box-sizing: border-box;
      outline: none;
      transition: all .2s linear;
      border: 1px solid #000;
      background: #FFF;
      box-shadow: 2px 1px 6px 1px rgba(0, 0, 0, 0.20);
    }

    .placeholder,
    .iconfont {
      position: absolute;
    }

    .placeholder {
      left: 80px;
      top: 12px;
      color: #999;
      pointer-events: none;
    }

    .iconfont {
      left: 15px;
      padding-right: 25px;
      width: 16px;
      height: 18px;
      top: 5px;
      color: #999;
      border-right: 1px solid #999;
      cursor: grab;
      &.icon-search {
        font-size: 22px;
        padding-top: 0px;
        top: 12px;
      }
    }
  }
</style>