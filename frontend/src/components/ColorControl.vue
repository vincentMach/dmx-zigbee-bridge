<template>
  <div>
    <h3>Channel {{ channel }}</h3>
    <label>Min: <input type="number" v-model.number="cfg.scale_min" /></label>
    <label>Max: <input type="number" v-model.number="cfg.scale_max" /></label>
    <label>Curve:
      <select v-model="cfg.filter_curve">
        <option>linear</option>
        <option>logarithmic</option>
      </select>
    </label>
    <button @click="save">Save</button>
  </div>
</template>
<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
export default {
  props: ['channel'],
  setup(props) {
    const cfg = ref({ channel: props.channel, scale_min: 0, scale_max: 1, filter_curve: 'linear' });
    const fetch = async () => {
      const res = await axios.get(`/api/color_control/channel/${props.channel}`);
      if(res.data) cfg.value = res.data;
    };
    const save = async () => { await axios.post('/api/color_control/channel', cfg.value); };
    onMounted(fetch);
    return { cfg, save };
  }
}
</script>
