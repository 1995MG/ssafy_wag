<template>
  <tr @click="onClickRedirect()">
    <td class="text-center">1</td>
    <td class="px-5">스파이더맨 노웨이홈 너무너무너무 기대된다!!</td>
    <td>sangjin</td>
    <td class="text-center">2021.11.17</td>
    <td class="text-center">7</td>
  </tr>
</template>

<script>
export default {
  name: 'ArticleListItem',
  methods:{
      onClickRedirect: function () {   
          this.$router.push({ name: 'ArticleDetail' })   
      }
    }
}
</script>

<style>

</style>