<template>
  <div>
    <label>Source:</label>
    <select v-model="src" @change="changeSource">
      <option value="dmx">DMX</option>
      <option value="artnet">Art-Net</option>
      <option value="sacn">sACN</option>
    </select>
  </div>
</template>
<script>
import { ref } from 'vue';
import axios from 'axios';
export default {
  setup() {
    const src = ref('dmx');
    const changeSource = async () => {
      await axios.post('/api/config', { source: src.value });
    };
    return { src, changeSource };
  }
}
</script>
