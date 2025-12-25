<script setup>
  import { ref, onMounted } from 'vue'  
  import { API_BASE_URL } from './services/api'

  const tickets = ref([])

  onMounted(async () => {
    const response = await fetch(`${API_BASE_URL}/api/tickets`)
    const data = await response.json()

    console.log("Dados do Backend",data)
    tickets.value = data
  })
</script>

<template>
  <main>
    <h1>Tickets</h1>
    <ul>
      <li v-for="ticket in tickets" :key="ticket.id">{{ ticket.id }} - {{ ticket.title }}</li>
    </ul>
  </main>
</template>

<style scoped>
  ul, li{
    text-decoration: none;
  }
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
