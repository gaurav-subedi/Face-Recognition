using System;
using System.Windows.Forms;
using System.Threading.Tasks;

namespace FaceHandDetectionUI
{
    public partial class Form1 : Form
    {
        private WebSocketClient _webSocketClient;

        public Form1()
        {
            InitializeComponent();

            // Subscribe to form events
            this.Load += Form1_Load;
            this.FormClosing += Form1_FormClosing;

            // Initialize the WebSocket client (adjust URL if needed)
            _webSocketClient = new WebSocketClient("ws://localhost:8765");
            _webSocketClient.DataReceived += OnDataReceived;
        }

        private async void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                Console.WriteLine("Connecting to WebSocket server...");
                await _webSocketClient.ConnectAsync();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Failed to connect to WebSocket server: " + ex.Message);
            }
        }

        private void OnDataReceived(int faceCount, string gesture)
        {
            // Ensure the UI is updated on the main thread
            if (InvokeRequired)
            {
                Invoke(new Action(() => OnDataReceived(faceCount, gesture)));
                return;
            }

            labelFaceCount.Text = "Faces Detected: " + faceCount;
            labelGesture.Text = "Gesture: " + gesture;

            Console.WriteLine("UI updated: Faces = " + faceCount + ", Gesture = " + gesture);
        }

        private async void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            await _webSocketClient.DisconnectAsync();
        }
    }
}
