<template>
  <div>
    <h5 class="fw-bold my-4">댓글</h5>
    <comment-list-item class="container"></comment-list-item>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'

export default {
  name: 'CommentList',
  components: {
    CommentListItem,
  }
}
</script>

<style>

</style>