<template>
    <div class="results">
      <table>
        <thead>
          <tr>
            <th>Razão Social</th>
            <th>Nome Fantasia</th>
            <th>CNPJ</th>
            <th>Registro ANS</th>
          </tr>
        </thead>
        <tbody>
          <operator-card
            v-for="operator in operators"
            :key="operator.CNPJ"
            :operator="operator"
          />
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import OperatorCard from './OperatorCard.vue';
  
  export default {
    name: 'OperatorList',
    components: {
      OperatorCard
    },
    props: {
      operators: {
        type: Array,
        required: true
      }
    }
  };
  </script>
  
  <style scoped>
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  th {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
    background-color: #f5f5f5;
  }
  </style>
  