<template>
    <tr>
      <td>{{ operator.Razao_Social }}</td>
      <td>{{ operator.Nome_Fantasia }}</td>
      <td>{{ operator.CNPJ }}</td>
      <td>{{ operator.Registro_ANS }}</td>
    </tr>
  </template>
  
  <script>
  export default {
    name: 'OperatorCard',
    props: {
      operator: {
        type: Object,
        required: true
      }
    }
  };
  </script>
  
  <style scoped>
  td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  </style>
  