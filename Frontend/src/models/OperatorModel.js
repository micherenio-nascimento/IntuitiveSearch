import axios from 'axios';

export default class OperatorModel {
  static async fetchAllOperators() {
    try {
      // Remova os < > da URL
      const response = await axios.get('http://127.0.0.1:8000/api/operators/search');
      return response.data.operators || [];
    } catch (error) {
      throw new Error('Erro ao carregar operadores: ' + error.message);
    }
  }

  static async searchOperators(query) {
    try {
      // Remova os < > da URL
      const response = await axios.get('http://127.0.0.1:8000/api/operators/search', {
        params: query ? { query } : {}
      });
      return response.data.operators || [];
    } catch (error) {
      throw new Error('Erro ao buscar operadores: ' + error.message);
    }
  }
}
