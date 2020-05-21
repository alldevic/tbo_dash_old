<script>
  import { DataTable, Pagination } from "carbon-components-svelte";

  let rows = [
    {
      id: "a",
      name: "Load Balancer 3",
      protocol: "HTTP",
      port: 3000,
      rule: "Round robin",
      attached_groups: "Kevins VM Groups",
      status: "Disabled"
    },
    {
      id: "b",
      name: "Load Balancer 1",
      protocol: "HTTP",
      port: 443,
      rule: "Round robin",
      attached_groups: "Maureens VM Groups",
      status: "Starting"
    },
    {
      id: "c",
      name: "Load Balancer 2",
      protocol: "HTTP",
      port: 80,
      rule: "DNS delegation",
      attached_groups: "Andrews VM Groups",
      status: "Active"
    },
    {
      id: "d",
      name: "Load Balancer 6",
      protocol: "HTTP",
      port: 3000,
      rule: "Round robin",
      attached_groups: "Marcs VM Groups",
      status: "Disabled"
    },
    {
      id: "e",
      name: "Load Balancer 4",
      protocol: "HTTP",
      port: 443,
      rule: "Round robin",
      attached_groups: "Mels VM Groups",
      status: "Starting"
    },
    {
      id: "f",
      name: "Load Balancer 5",
      protocol: "HTTP",
      port: 80,
      rule: "DNS delegation",
      attached_groups: "Ronjas VM Groups",
      status: "Active"
    }
  ];
  let headers = [
    { key: "name", value: "Name" },
    { key: "protocol", value: "Protocol" },
    { key: "port", value: "Port" },
    { key: "rule", value: "Rule" },
    { key: "attached_groups", value: "Attached Groups" },
    { key: "status", value: "Status" }
  ];
</script>

<style lang="scss" global>
  @import "carbon-components/scss/components/pagination/pagination";
  @import "carbon-components/scss/components/data-table/data-table";
</style>

<svelte:head>
  <title>TBO Dashboard</title>
</svelte:head>
<DataTable description="qweqe" title="qweqweqweqwee" {rows} {headers} />
<Pagination totalItems={103} />
