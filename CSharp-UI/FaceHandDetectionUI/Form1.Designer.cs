namespace FaceHandDetectionUI
{
    partial class Form1
    {
        private System.ComponentModel.IContainer components = null;
        private System.Windows.Forms.Label labelFaceCount;
        private System.Windows.Forms.Label labelGesture;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        private void InitializeComponent()
        {
            this.labelFaceCount = new System.Windows.Forms.Label();
            this.labelGesture = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // labelFaceCount
            // 
            this.labelFaceCount.AutoSize = true;
            this.labelFaceCount.Font = new System.Drawing.Font("Arial", 12F, System.Drawing.FontStyle.Bold);
            this.labelFaceCount.Location = new System.Drawing.Point(20, 20);
            this.labelFaceCount.Name = "labelFaceCount";
            this.labelFaceCount.Size = new System.Drawing.Size(180, 20);
            this.labelFaceCount.TabIndex = 0;
            this.labelFaceCount.Text = "Faces Detected: 0";
            // 
            // labelGesture
            // 
            this.labelGesture.AutoSize = true;
            this.labelGesture.Font = new System.Drawing.Font("Arial", 12F, System.Drawing.FontStyle.Bold);
            this.labelGesture.Location = new System.Drawing.Point(20, 60);
            this.labelGesture.Name = "labelGesture";
            this.labelGesture.Size = new System.Drawing.Size(130, 20);
            this.labelGesture.TabIndex = 1;
            this.labelGesture.Text = "Gesture: None";
            // 
            // Form1
            // 
            this.ClientSize = new System.Drawing.Size(400, 200);
            this.Controls.Add(this.labelGesture);
            this.Controls.Add(this.labelFaceCount);
            this.Name = "Form1";
            this.Text = "Face & Gesture Detection UI";
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        #endregion
    }
}
