<template>
  <tr @click="onClickRedirect()">
    <td class="text-center">{{ article.id }}</td>
    <td class="px-5">{{ article.title }}</td>
    <td>{{ article.username }}</td>
    <td class="text-center">{{ article.created_at }}</td>
    <td class="text-center">7</td>
  </tr>
</template>

<script>
export default {
  name: 'ArticleListItem',
  methods:{
    onClickRedirect: function () {   
        this.$router.push({ name: 'ArticleDetail' })   
    },
  },
  props: {
    article: Object
  },
  // created: function () {
  //   console.log(this.article)
  // }
}
</script>

<style>

</style>