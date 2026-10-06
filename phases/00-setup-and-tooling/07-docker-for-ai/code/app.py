import torch
import numpy as np

print("=== DOCKER ICINDEN SELAMLAR ===")
print(f"PyTorch Sürümü: {torch.__version__}")
print(f"CUDA Mevcut mu: {torch.cuda.is_available()} (CPU modu aktif)")

# Basit bir matris çarpımı
x = torch.rand(3, 3)
y = torch.rand(3, 3)
z = torch.matmul(x, y)

print("\nÖrnek Tensör Çarpımı Başarılı:")
print(z)
