<script>
  import Table from "../components/Table.svelte";
  import io from "socket.io-client";

  let rows = [];
  const headers = [
    { key: "time", value: "Time" },
    { key: "cid", value: "Client ID" },
    { key: "latency", value: "Latency" }
  ];

  const socket = io("http://localhost:8000", { path: "/api/v1/wsdash" });

  socket.on("connect", () => {
    console.log("Connected, id=", socket.id);
  });

  let rowId = 0;

  socket.on("pong", function(ms) {
    rows = [
      {
        id: rowId++,
        cid: socket.id,
        latency: ms,
        time: new Date(Date.now()).toLocaleString()
      },
      ...rows
    ];
  });
</script>

<svelte:head>
  <title>TBO Dashboard</title>
</svelte:head>

<Table {rows} {headers} />
