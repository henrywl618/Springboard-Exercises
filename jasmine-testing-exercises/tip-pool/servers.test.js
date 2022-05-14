describe("Servers test (with setup and tear-down)", function() {
  beforeEach(function () {
    // initialization logic
    serverNameInput.value = 'Alice';
    serverID = 0;
  });

  it('should add a new server to allServers on submitServerInfo()', function () {
    submitServerInfo();

    expect(Object.keys(allServers).length).toEqual(1);
    expect(allServers['server' + serverId].serverName).toEqual('Alice');
  });

  it('should create a serverTable from allServers array', function(){
    allServers = {
      server1: {serverName: 'Alice'},
      server2: {serverName: 'Henry'},
    };
    updateServerTable();
    expect(document.querySelectorAll('#serverTable tbody tr').length).toBe(2);
    expect(document.querySelectorAll('#serverTable tbody tr td').length).toBe(6);
    expect(document.querySelectorAll('#server2 td')[0].innerText).toEqual('Henry');
    expect(document.querySelectorAll('#server2 td')[1].innerText).toEqual('$0.00');
  });

  it('should not update the table if the server input is empty', function() {
    console.log('run');
    submitServerInfo();
    serverNameInput.value = '';
    submitServerInfo();
    expect(Object.keys(allServers).length).toEqual(1);
    expect(allServers['server' + serverId + 1]).toBeUndefined();
  });

  afterEach(function() {
   allServers = {};

   updateServerTable();
  });
});
