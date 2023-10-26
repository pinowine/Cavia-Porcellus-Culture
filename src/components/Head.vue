<template>
  <div id="headmenu">
    <div class="container">
      <router-link to="/"><img id='logo' src="../assets/img/logo.svg"></router-link>
      <Selector
        :data="selectorData"
        @setItemValue="setItemValue"
      />
      
        <label><router-link to="/loginpage">News</router-link></label>
        <label><router-link to="/loginpage">Bussiness</router-link></label>
        <label><router-link to="/loginpage">AboutUs</router-link></label>
    </div>
  </div>
</template>
  
<script>
  
import selectorData from '../data/selector.js';

import { ref } from 'vue';

export default {
name: 'headmenu',
setup () {
    
    const val = ref('');

    const setItemValue = (value) => {
    val.value = value;

    console.log(val.value);
    }

    return {
    selectorData,
    setItemValue
    }
}
}
</script>
  
<style lang="scss" scoped>
    #headmenu {
      border-bottom: 1px solid #000;
      background: #F4F4F4;
      top:-10px;
      width: 100%;
      height: 75px;
      position: fixed;
      z-index: 99999999;
      transition: all 0.3s ease-in-out;
    }
    .container {
      padding: {
        left:10px;
        right: 20px;
      };
      display: flex;
      flex: {
        direction: row;
      }
      align-items: flex-start;
      justify-content: space-between;
      height: 100%;

      .selector {
        padding-top:20px;
      }

      
      #logo {
        padding-top: 7px;
        width: 65px;
        padding-left: 10px;
        display: inline-block;
        transition: all 0.3s ease-in-out;

        &:hover {
          transform: scale(1.01);
          transition: all 0.3s ease-in-out;
          animation-name: zoomin;
          animation-duration: 0.5s;
          animation-iteration-count: infinite;
          animation-direction: alternate;
        }
      }

      label {
        margin-top: 25px;
        padding: {
          top:5px;
          bottom: 5px;
          left: 20px;
          right: 20px;
        }
        font-size: 15px;
        border-radius: 10px;
        border: 2px solid #000;
        background: #FFF;
        box-shadow: 1px 2px 5px 1px rgba(0, 0, 0, 0.25);
        transition: all 0.3s ease;

        &:hover {
          transform: scale(1.05);
          transition: all 0.5s ease;
          animation-name: zoomin;
          animation-duration: 0.5s;
          animation-iteration-count: infinite;
          animation-direction: alternate;
        }

        @keyframes zoomin {
          from {
            scale: 1.05;
          }
          to {
            scale: 1.08;
          }
        }
        
      }
    
    }

</style>