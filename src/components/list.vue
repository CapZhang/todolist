<template >
  <section>
    <ul class="todo-list" v-show="todoList.length">
      <li
        class="todo-item"
        v-for="(item, index) in todoList"
        v-bind:key="index + item.name"
      >
        <span>{{ index + 1 }}.</span>
        <p>
          {{ item.name }}<br /><span class="todo-time" v-if="item.deadline">截止时间: {{ item.deadline }}</span
          >
        </p>
        <button @click="removeItem(index)">完成</button>
      </li>
    </ul>
    <div class="todo-nodata" v-show="!todoList.length">
      恭喜你完成所有内容，请继续添加！！
    </div>
  </section>
</template>

<script>
export default {
  computed: {
    todoList: function () {
      return this.$store.state.items;
    },
  },
  methods: {
    removeItem(index) {
      this.$store.dispatch("removeItem", index);
    },
  },
};
</script>