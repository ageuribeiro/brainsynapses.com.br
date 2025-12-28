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
      <li v-for="ticket in tickets" :key="ticket.id">{{ ticket.id }} - {{ ticket.title }} - {{ ticket.description }}</li>
    </ul>
  </main>
</template>


