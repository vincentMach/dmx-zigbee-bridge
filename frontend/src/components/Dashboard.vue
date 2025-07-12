<template>
  <div>
    <h1>DMX Real-Time Dashboard</h1>
    <InputSourceSelector />
    <div v-for="msg in messages" :key="msg.universe">
      <strong>{{ msg.protocol }}</strong> U{{ msg.universe }}: {{ msg.channels.slice(0,16) }}
    </div>
  </div>
</template>
<script>
import { ref, onMounted } from 'vue';
import InputSourceSelector from './InputSourceSelector.vue';
export default {
  components: { InputSourceSelector },
  setup() {
    const messages = ref([]);
    onMounted(() => {
      const ws = new WebSocket('ws://' + window.location.hostname + '/ws/dmx');
      ws.onmessage = e => {
        messages.value.unshift(JSON.parse(e.data));
        if (messages.value.length > 5) messages.value.pop();
      };
    });
    return { messages };
  }
}
</script>
