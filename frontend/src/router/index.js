import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '../components/Dashboard.vue';
import ScenesManager from '../components/ScenesManager.vue';
import DeviceList from '../components/DeviceList.vue';
import ColorControl from '../components/ColorControl.vue';

const routes = [
  { path: '/', component: Dashboard },
  { path: '/scenes', component: ScenesManager },
  { path: '/devices', component: DeviceList },
  { path: '/color-control', component: ColorControl }
];

export default createRouter({
  history: createWebHistory(),
  routes
});
