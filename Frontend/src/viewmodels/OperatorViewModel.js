import OperatorModel from '../models/OperatorModel';

export default class OperatorViewModel {
  constructor() {
    this.operators = [];
    this.loading = false;
    this.error = null;
    this.searchQuery = '';
  }

  async loadInitialData() {
    this.loading = true;
    this.error = null;
    try {
      this.operators = await OperatorModel.fetchAllOperators();
    } catch (err) {
      this.error = err.message;
    } finally {
      this.loading = false;
    }
  }

  async search() {
    this.loading = true;
    this.error = null;
    try {
      this.operators = await OperatorModel.searchOperators(this.searchQuery.trim());
    } catch (err) {
      this.error = err.message;
    } finally {
      this.loading = false;
    }
  }

  setSearchQuery(query) {
    this.searchQuery = query;
  }
}
