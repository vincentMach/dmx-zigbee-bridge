<template>
  <div>
    <nav>
      <router-link to="/">Dashboard</router-link> |
      <router-link to="/scenes">Scenes</router-link> |
      <router-link to="/devices">Devices</router-link> |
      <router-link to="/color-control">Color Control</router-link>
    </nav>
    <router-view />
  </div>
</template>
