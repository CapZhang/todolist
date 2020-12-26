<template>
  <section>
    <ul class="sub-todo-list">
      <li
        class="sub-todo-item"
        v-for="(item, index) in sublist"
        :key="index + item.uuid"
      >
          <i
            class="fa fa-square-o todo-done"
            aria-hidden="true"
            @click="updateItem(item, 'done')"
            title="完成"
          ></i>
          <i
            v-if="item.status != 'doing'"
            class="fa fa-play-circle-o fa-2x todo-start"
            aria-hidden="true"
            @click="updateItem(item, 'doing')"
            title="开始"
          ></i>
          <i
            v-else-if="item.status == 'doing'"
            class="fa fa-spinner fa-pulse fa-2x todo-start"
            aria-hidden="true"
            @click="updateItem(item, 'stop')"
            title="暂停"
          ></i>
          <p>
            <span>{{ index + 1 }}. {{ item.name }}</span
            ><br />
            <span class="todo-time" v-if="item.deadline"
              >截止时间: {{ chGMT(item.deadline) }}</span
            >
          </p>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: "subItems",
  props: {
    sublist: {
      type: Array,
    },
  },
  data() {
    return {};
  },
};
</script>