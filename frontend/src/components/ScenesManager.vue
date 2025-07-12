<template>
  <div>
    <h2>Scenes</h2>
    <ul>
      <li v-for="scene in scenes" :key="scene.id">
        {{ scene.name }}
        <button @click="deleteScene(scene.id)">Delete</button>
      </li>
    </ul>
    <input v-model="newName" placeholder="New scene name" />
    <button @click="createScene">Create Scene</button>
  </div>
</template>
<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
export default {
  setup() {
    const scenes = ref([]);
    const newName = ref('');
    const fetchScenes = async () => {
      scenes.value = (await axios.get('/api/scenes')).data;
    };
    const createScene = async () => {
      if (!newName.value) return;
      await axios.post('/api/scenes', { name: newName.value, mappings: '{}' });
      newName.value = '';
      fetchScenes();
    };
    const deleteScene = async id => {
      await axios.delete(`/api/scenes/${id}`);
      fetchScenes();
    };
    onMounted(fetchScenes);
    return { scenes, newName, createScene, deleteScene };
  }
}
</script>
