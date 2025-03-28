<template>
    <div class="search-container">
        <input
        :value="query"
        @input="$emit('update:query', $event.target.value)"
        @keyup.enter="$emit('search')"
        placeholder="Digite Razão Social, Nome Fantasia, CNPJ ou Registro ANS"
        class="search-input"
      />
      <button @click="$emit('search')" class="search-button">
        Buscar
      </button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SearchBar',
    props: {
      query: {
        type: String,
        default: ''
      }
    },
    emits: ['update:query', 'search']
  };
  </script>
  
  <style scoped>
  .search-container {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
  }
  
  .search-input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  .search-button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .search-button:hover {
    background-color: #0056b3;
  }
  </style>
  