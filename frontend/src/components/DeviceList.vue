<template>
  <div>
    <h2>Zigbee Devices</h2>
    <button @click="discover">Discover Devices</button>
    <ul>
      <li v-for="dev in devices" :key="dev.id">{{ dev.name }}</li>
    </ul>
  </div>
</template>
<script>
import { ref } from 'vue';
import axios from 'axios';
export default {
  setup() {
    const devices = ref([]);
    const fetch = async () => { devices.value = (await axios.get('/api/devices')).data; };
    const discover = async () => {
      await axios.post('/api/devices/discover');
      setTimeout(fetch, 1000);
    };
    fetch();
    return { devices, discover };
  }
}
</script>
