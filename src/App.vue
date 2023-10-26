<template>
  <headmenu/>
  <RouterView></RouterView>
  <bottom/>
</template>

<script>

import headmenu from './components/Head';
import curser from './components/Curser';
import bottom from './components/Bottom';

export default {

  name: 'App',
  components: {
    headmenu,
    curser,
    bottom
  }
}

</script>

<style>
*::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.1);
  border-radius: 0;
}

*::-webkit-scrollbar {
  -webkit-appearance: none;
  width: 6px;
  height: 6px;
}

*::-webkit-scrollbar-thumb {
  cursor: pointer;
  border-radius: 5px;
  background: rgba(0, 0, 0, 0.15);
  transition: color 0.2s ease;
}

a {
  text-decoration: none;
  color: black;
}
</style>