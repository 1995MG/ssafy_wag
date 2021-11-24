<template>
  <tr @click="toDetail(article)" class="align-middle">
    <td class="text-center">{{ article.id }}</td>
    <td class="px-5">{{ article.title }} [{{this.commentCount}}]</td>
    <td>{{ article.username }}</td>
    <td class="text-center">{{ articleCreatedAt }}</td>
    <td class="text-center">{{ likeCount }}</td>
  </tr>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ArticleListItem',
  data: function () {
    return {
      likeCount: null,
      commentCount: 0,
      articleCreatedAt: null,
    }
  },
  methods:{
    toDetail: function (article) {   
        this.$router.push({ name: 'ArticleDetail', params: {articleId: article.id} })   
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getLikes: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.article.id}/likes/`,
        headers: this.setToken()
      })
        .then((res) => {
          this.likeCount = res.data.count
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getCommentCount: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.article.id}/comment/`,
        headers: this.setToken()
      })
        .then((res) => {
          this.commentCount = res.data.length
        })
        .catch((err) => {
          this.commentCount = 0
          console.log(err)
        })
    }
  },
  props: {
    article: Object
  },
  created: function () {
    console.log(this.article)
    this.getLikes()
    this.getCommentCount()
    this.articleCreatedAt = this.article.created_at.substring(0, 10) + ' ' + this.article.created_at.substring(11, 16)
  }
}
</script>

<style>

</style>