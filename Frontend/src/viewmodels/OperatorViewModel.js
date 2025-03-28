import { reactive } from 'vue';
import OperatorModel from '../models/OperatorModel';

export default function createOperatorViewModel() {
  const state = reactive({
    operators: [],
    loading: false,
    error: null,
    searchQuery: ''
  });

  async function loadInitialData() {
    state.loading = true;
    state.error = null;
    try {
      state.operators = await OperatorModel.fetchAllOperators();
    } catch (err) {
      state.error = err.message;
    } finally {
      state.loading = false;
    }
  }

  async function search() {
    state.loading = true;
    state.error = null;
    try {
      state.operators = await OperatorModel.searchOperators(state.searchQuery.trim());
    } catch (err) {
      state.error = err.message;
    } finally {
      state.loading = false;
    }
  }

  return {
    state,
    loadInitialData,
    search
  };
}