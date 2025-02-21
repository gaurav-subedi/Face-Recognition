using System;
using System.Net.WebSockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

public class WebSocketClient
{
    private ClientWebSocket _client;
    private readonly Uri _serverUri;
    public event Action<int, string> DataReceived;

    public WebSocketClient(string serverUrl)
    {
        _serverUri = new Uri(serverUrl);
    }

    public async Task ConnectAsync()
    {
        // Continuously attempt to connect
        while (true)
        {
            _client = new ClientWebSocket();
            try
            {
                await _client.ConnectAsync(_serverUri, CancellationToken.None);
                Console.WriteLine("Connected to Python WebSocket Server.");
                await ReceiveMessagesAsync(); // Listen for messages
            }
            catch (Exception ex)
            {
                Console.WriteLine("WebSocket Connection Error: " + ex.Message);
                Console.WriteLine("Retrying connection in 5 seconds...");
                await Task.Delay(5000);
            }
        }
    }

    private async Task ReceiveMessagesAsync()
    {
        var buffer = new byte[4096]; // Increased buffer size
        while (_client.State == WebSocketState.Open)
        {
            var result = await _client.ReceiveAsync(new ArraySegment<byte>(buffer), CancellationToken.None);
            string message = Encoding.UTF8.GetString(buffer, 0, result.Count);
            Console.WriteLine("Received message: " + message);

            try
            {
                var jsonData = JObject.Parse(message);
                int facesDetected = jsonData["faces_detected"].ToObject<int>();
                string gesture = jsonData["gesture"].ToString();
                Console.WriteLine("Parsed message: Faces = " + facesDetected + ", Gesture = " + gesture);

                DataReceived?.Invoke(facesDetected, gesture);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error parsing JSON: " + ex.Message);
            }
        }
    }

    public async Task DisconnectAsync()
    {
        if (_client != null && _client.State == WebSocketState.Open)
        {
            await _client.CloseAsync(WebSocketCloseStatus.NormalClosure, "Client disconnected", CancellationToken.None);
        }
    }
}
