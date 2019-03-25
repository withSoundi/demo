<template>
    <div>
        <h1></h1>
    </div>
</template>

<script>
export default {
  name: 'chartItem',
  props: {
    items: Array,
    default () {
      return []
    },
  }
}
</script>