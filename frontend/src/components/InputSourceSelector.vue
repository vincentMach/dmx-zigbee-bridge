<template>
  <div>
    <label>Source:</label>
    <select v-model="source" @change="update">
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
    const source = ref('dmx');
    const update = async () => { await axios.post('/api/config', { source: source.value }); };
    return { source, update };
  }
}
</script>
