<template>
  <div class="container">
    <h1>Busca de Operadoras</h1>
    
    <search-bar
      v-model:query="viewModel.state.searchQuery"
      @search="viewModel.search"
    />
    
    <div v-if="viewModel.state.loading" class="loading">Carregando...</div>
    
    <operator-list
      v-if="viewModel.state.operators.length"
      :operators="viewModel.state.operators"
    />
    
    <div v-if="viewModel.state.error" class="error">{{ viewModel.state.error }}</div>
    <div v-if="!viewModel.state.loading && !viewModel.state.operators.length && viewModel.state.searchQuery" class="no-results">
      Nenhum resultado encontrado
    </div>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue';
import OperatorList from './components/OperatorList.vue';
import createOperatorViewModel from './viewmodels/OperatorViewModel';

export default {
  name: 'App',
  components: {
    SearchBar,
    OperatorList
  },
  setup() {
    const viewModel = createOperatorViewModel();
    viewModel.loadInitialData();
    return { viewModel };
  }
};
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.loading {
  text-align: center;
  padding: 20px;
}

.error {
  color: red;
  text-align: center;
  padding: 20px;
}

.no-results {
  text-align: center;
  padding: 20px;
  color: #666;
}
</style>