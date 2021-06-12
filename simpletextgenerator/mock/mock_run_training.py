import sys
from time import sleep

time_between_prints = 0.05

if __name__ == "__main__":
    pass

print(
    "2021-06-10 14:45:27.256995: W tensorflow/stream_executor/platform/default/dso_loader.cc:60] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory" +
    "\n2021-06-10 14:45:27.257051: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.", file = sys.stderr)
sleep(time_between_prints)
print("Found 1 projects to train.")
sleep(time_between_prints)
print(
    "2021-06-10 14:45:31.926249: I tensorflow/compiler/jit/xla_cpu_device.cc:41] Not creating XLA devices, tf_xla_enable_xla_devices not set", file = sys.stderr)
sleep(time_between_prints)
print(
    "2021-06-10 14:45:31.928021: W tensorflow/stream_executor/platform/default/dso_loader.cc:60] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory" +
    "\n2021-06-10 14:45:31.928055: W tensorflow/stream_executor/cuda/cuda_driver.cc:326] failed call to cuInit: UNKNOWN ERROR (303, file = sys.stderr)" +
    "\n2021-06-10 14:45:31.928101: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (galliumos): /proc/driver/nvidia/version does not exist")
sleep(time_between_prints)
print(
    "2021-06-10 14:45:31.928497: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN, file = sys.stderr) to use the following CPU instructions in performance-critical operations:  AVX2 FMA" +
    "\nTo enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.")
sleep(time_between_prints)
print(
    "2021-06-10 14:45:31.928983: I tensorflow/compiler/jit/xla_gpu_device.cc:99] Not creating XLA devices, tf_xla_enable_xla_devices not set", file = sys.stderr)
sleep(time_between_prints)
print("Loading project ramen_test2" +
      "\nLoading model")
sleep(time_between_prints)
print("199 texts collected.")
sleep(time_between_prints)
print("Training on 8,669 character sequences.")
sleep(time_between_prints)
print(
    "2021-06-10 14:45:34.089746: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:116] None of the MLIR optimization passes are enabled (registered 2, file = sys.stderr)")
sleep(time_between_prints)
print(
    "2021-06-10 14:45:34.106405: I tensorflow/core/platform/profile_utils/cpu_utils.cc:112] CPU Frequency: 1695965000 Hz", file = sys.stderr)
sleep(time_between_prints)
print(
    "2021-06-10 14:45:38.800244: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 7290880 exceeds 10% of free system memory.", file = sys.stderr)
sleep(time_between_prints)
print(
    "2021-06-10 14:45:38.814580: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 7290880 exceeds 10% of free system memory.", file = sys.stderr)
sleep(time_between_prints)
print(
    "2021-06-10 14:45:38.832801: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 7290880 exceeds 10% of free system memory.", file = sys.stderr)
sleep(time_between_prints)
print(
    "2021-06-10 14:45:38.838225: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 7290880 exceeds 10% of free system memory." +
    "\n2021-06-10 14:45:38.838225: W tensorflow/core/framework/cpu_allocator_impl.cc:80] Allocation of 7290880 exceeds 10% of free system memory.", file = sys.stderr)
sleep(time_between_prints)
print("1/67 [..............................]")
sleep(time_between_prints)
print("- ETA: 5:42 - loss: 0.7759" +
      "\n2/67 [..............................]")
sleep(time_between_prints)
print("- ETA: 18s - loss: 0.7902" +
      "\n3/67 [>.............................]")
sleep(time_between_prints)
print("- ETA: 18s - loss: 0.7899" +
      "\n4/67 [>.............................]")
sleep(time_between_prints)
print("- ETA: 17s - loss: 0.7767" +
      "\n5/67 [=>............................]")
sleep(time_between_prints)
print("- ETA: 17s - loss: 0.7703" +
      "\n6/67 [=>............................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.7643" +
      "\n7/67 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.7597" +
      "\n8/67 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.7587" +
      "\n9/67 [===>..........................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.7587" +
      "\n10/67 [===>..........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.7584" +
      "\n11/67 [===>..........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.7584" +
      "\n12/67 [====>.........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.7593" +
      "\n13/67 [====>.........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.7609" +
      "\n14/67 [=====>........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.7620" +
      "\n15/67 [=====>........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.7636" +
      "\n16/67 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.7653" +
      "\n17/67 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.7671" +
      "\n18/67 [=======>......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.7683" +
      "\n19/67 [=======>......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.7695" +
      "\n20/67 [=======>......................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.7702" +
      "\n21/67 [========>.....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.7711" +
      "\n22/67 [========>.....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.7717" +
      "\n23/67 [=========>....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.7724" +
      "\n24/67 [=========>....................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.7733" +
      "\n25/67 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.7737" +
      "\n26/67 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.7742" +
      "\n27/67 [===========>..................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.7746" +
      "\n28/67 [===========>..................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.7750" +
      "\n29/67 [===========>..................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.7756" +
      "\n30/67 [============>.................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.7762" +
      "\n31/67 [============>.................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.7770" +
      "\n32/67 [=============>................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.7776" +
      "\n33/67 [=============>................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.7781" +
      "\n34/67 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.7785" +
      "\n35/67 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.7789" +
      "\n36/67 [===============>..............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.7792" +
      "\n37/67 [===============>..............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.7796" +
      "\n38/67 [================>.............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.7800" +
      "\n39/67 [================>.............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.7804" +
      "\n40/67 [================>.............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.7809" +
      "\n41/67 [=================>............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.7813" +
      "\n42/67 [=================>............]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.7816" +
      "\n43/67 [==================>...........]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.7820" +
      "\n44/67 [==================>...........]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.7824" +
      "\n45/67 [===================>..........]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.7829" +
      "\n46/67 [===================>..........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.7834" +
      "\n47/67 [====================>.........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.7839" +
      "\n48/67 [====================>.........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.7844" +
      "\n49/67 [====================>.........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.7849" +
      "\n50/67 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.7853" +
      "\n51/67 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.7857" +
      "\n52/67 [======================>.......]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.7862" +
      "\n53/67 [======================>.......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.7866" +
      "\n54/67 [=======================>......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.7870" +
      "\n55/67 [=======================>......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.7875" +
      "\n56/67 [========================>.....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.7879" +
      "\n57/67 [========================>.....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.7883" +
      "\n58/67 [========================>.....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.7888" +
      "\n59/67 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.7892" +
      "\n60/67 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.7896" +
      "\n61/67 [==========================>...]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.7899" +
      "\n62/67 [==========================>...] - ETA: 1s - loss: 0.7902" +
      "\n63/67 [===========================>..] - ETA: 1s - loss: 0.7905" +
      "\n64/67 [===========================>..] - ETA: 0s - loss: 0.7908" +
      "\n65/67 [============================>.]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.7911" +
      "\n66/67 [============================>.]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.7913" +
      "\n67/67 [==============================]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.7916" +
      "\n67/67 [==============================]")
sleep(time_between_prints)
print("- 28s 345ms/step - loss: 0.7918 - val_loss: 0.7932")
sleep(time_between_prints)
print("####################" +
      "\nTemperature: 0.2" +
      "\n  ####################")
sleep(time_between_prints)
print("Nissin,Cup Noodles Beef Flavor Instant Noodles,Pack,Singapore,5,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Shoyu Flavour,Cup,Singapore,3.5,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Chicken Flavor,Pack,Singapore,5," +
      "\n" +
      "\n#################### " +
      "\nTemperature: 0.5" +
      "\n####################")
sleep(time_between_prints)
print("Magni,Memid Snack Flavour,Cup,China,0,")
sleep(time_between_prints)
print("Soup Noodles Chicken Flavour,Cup,Malaysia,Cup,Malaysi,3.25,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Shoyu Ramen,Pack,Germany,3.75," +
      "\n" +
      "\n####################" +
      "\nTemperature: 1.0" +
      "\n####################")
sleep(time_between_prints)
print("Nissin,Cup Noodlishe Flavor Stew Ramen,Pack,India,3.5,")
sleep(time_between_prints)
print("Nissin,Mexihoman,Soba Noodles Chicken Flavor Instant,St,Cup,Morel,3.75,")
sleep(time_between_prints)
print("Amani Ramen,Nog Chicken Fold Snackshi Flavour,Pack,Indon,3.75,")
sleep(time_between_prints)
print("Generating text to output file.")
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:04<00:19,  4.85s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:07<00:10,  3.58s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:10<00:06,  3.29s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:13<00:03,  3.12s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:16<00:00,  3.09s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:16<00:00,  3.27s/it]", file = sys.stderr)
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:00<00:02,  1.85it/s]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:05<00:08,  2.89s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:07<00:05,  2.82s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:11<00:03,  3.01s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:13<00:00,  2.71s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:13<00:00,  2.66s/it]", file = sys.stderr)
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:05<00:23,  5.90s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:08<00:11,  3.69s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:13<00:08,  4.27s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:16<00:03,  3.81s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:18<00:00,  3.15s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:18<00:00,  3.62s/it]", file = sys.stderr)
sleep(time_between_prints)
print("Saving model" +
      "\nSaving model current")
sleep(time_between_prints)
print("Saving model current")
sleep(time_between_prints)
print("Updating state")
sleep(time_between_prints)
print("from stdout:")
sleep(time_between_prints)
print("199 texts collected.")
sleep(time_between_prints)
print("Training on 8,758 character sequences.")
sleep(time_between_prints)
print("1/68 [..............................]")
sleep(time_between_prints)
print("- ETA: 21s - loss: 0.7821" +
      "\n2/68 [..............................]")
sleep(time_between_prints)
print("- ETA: 17s - loss: 0.7741" +
      "\n3/68 [>.............................]")
sleep(time_between_prints)
print("- ETA: 17s - loss: 0.7249" +
      "\n4/68 [>.............................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.7526" +
      "\n5/68 [=>............................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.7564" +
      "\n6/68 [=>............................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.7313" +
      "\n7/68 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.7204" +
      "\n8/68 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.7286" +
      "\n9/68 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.7253" +
      "\n10/68 [===>..........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.7257" +
      "\n11/68 [===>..........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.7240" +
      "\n12/68 [====>.........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.7194" +
      "\n13/68 [====>.........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.7116" +
      "\n14/68 [=====>........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.7195" +
      "\n15/68 [=====>........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.7136" +
      "\n16/68 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.7086" +
      "\n17/68 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.7218" +
      "\n18/68 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.7277" +
      "\n19/68 [=======>......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.7333" +
      "\n20/68 [=======>......................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.7332" +
      "\n21/68 [========>.....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.7336" +
      "\n22/68 [========>.....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.7322" +
      "\n23/68 [=========>....................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.7277" +
      "\n24/68 [=========>....................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.7291" +
      "\n25/68 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.7246" +
      "\n26/68 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.7228" +
      "\n27/68 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.7128" +
      "\n28/68 [===========>..................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.7172" +
      "\n29/68 [===========>..................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.7159" +
      "\n30/68 [============>.................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.7142" +
      "\n31/68 [============>.................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.7181" +
      "\n32/68 [=============>................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.7193" +
      "\n33/68 [=============>................] - ETA: 9s - loss: 0.7192" +
      "\n34/68 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.7115" +
      "\n35/68 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.7154" +
      "\n36/68 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.7148" +
      "\n37/68 [===============>..............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.7156" +
      "\n38/68 [===============>..............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.7155" +
      "\n39/68 [================>.............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.7163" +
      "\n40/68 [================>.............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.7132" +
      "\n41/68 [=================>............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.7118" +
      "\n42/68 [=================>............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.7098" +
      "\n43/68 [=================>............]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.7053" +
      "\n44/68 [==================>...........] - ETA: 6s - loss: 0.7044" +
      "\n45/68 [==================>...........]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.7055" +
      "\n46/68 [===================>..........]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.7066" +
      "\n47/68 [===================>..........]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.7059" +
      "\n48/68 [====================>.........] - ETA: 5s - loss: 0.7045" +
      "\n49/68 [====================>.........] - ETA: 5s - loss: 0.7106" +
      "\n50/68 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.7103" +
      "\n51/68 [=====================>........] - ETA: 5s - loss: 0.7091" +
      "\n52/68 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.7076" +
      "\n53/68 [======================>.......]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.7078" +
      "\n54/68 [======================>.......]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.7093" +
      "\n55/68 [=======================>......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.7106" +
      "\n56/68 [=======================>......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.7110" +
      "\n57/68 [========================>.....]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.7118" +
      "\n58/68 [========================>.....]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.7127" +
      "\n59/68 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.7105" +
      "\n60/68 [=========================>....] - ETA: 54:32 - loss: 0.7113" +
      "\n")
sleep(time_between_prints)
print("61/68 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 46:55 - loss: 0.7125" +
      "\n62/68 [==========================>...] - ETA: 39:33 - loss: 0.7125" +
      "\n63/68 [==========================>...]")
sleep(time_between_prints)
print("- ETA: 32:26 - loss: 0.7092" +
      "\n64/68 [===========================>..]")
sleep(time_between_prints)
print("- ETA: 25:32 - loss: 0.7085" +
      "\n65/68 [===========================>..]")
sleep(time_between_prints)
print("- ETA: 18:51 - loss: 0.7090" +
      "\n66/68 [============================>.]")
sleep(time_between_prints)
print("- ETA: 12:22 - loss: 0.7089" +
      "\n67/68 [============================>.]")
sleep(time_between_prints)
print("- ETA: 6:05 - loss: 0.7072" +
      "\n68/68 [==============================]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.7083" +
      "\n68/68 [==============================]")
sleep(time_between_prints)
print("- 24137s 360s/step - loss: 0.7083 - val_loss: 0.6924")
sleep(time_between_prints)
print("####################" +
      "\nTemperature: 0.2" +
      "\n####################")
sleep(time_between_prints)
print("Nissin,Cup Noodles Chicken Flavour Ramen Noodle,Bowl,South Korea,5,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Chicken Flavor Instant Noodles,Pack,Singapore,5,")
sleep(time_between_prints)
print("Maggi,Cup,South Korea,Cup,Singapore,5," +
      "\n" +
      "\n####################" +
      "\nTemperature: 0.5" +
      "\n####################")
sleep(time_between_prints)
print("KOKA,Creamy Soup With Seawa Pork Base Spicy,Pack,South Korea,5,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Beef Flavour Ramen,Pack,South Korea,5,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Chicken Flavour,Cup,USA,5," +
      "\n" +
      "\n####################" +
      "\nTemperature: 1.0" +
      "\n####################")
sleep(time_between_prints)
print("ParyPorkks Kong,Chanshuha Mai Secret Noodle,Pack,South Korea,4,")
sleep(time_between_prints)
print("Samyang Fureal Buld Tom Yum & Seafood,Bowl,USA,5,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Dakga Fujiwara Ching's,Sesame Soup,Black Flavour,Cup,USA,Caro Singapore,5,")
sleep(time_between_prints)
print("Generating text to output file.")
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:01<00:04,  1.23s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:02<00:03,  1.18s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:06<00:04,  2.41s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:08<00:02,  2.37s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:12<00:00,  2.87s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:12<00:00,  2.46s/it]", file = sys.stderr)
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:02<00:11,  2.89s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:08<00:13,  4.37s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:12<00:08,  4.36s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:14<00:03,  3.34s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:19<00:00,  3.89s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:19<00:00,  3.86s/it]", file = sys.stderr)
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:05<00:20,  5.22s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:08<00:12,  4.23s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:10<00:06,  3.10s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:12<00:02,  2.85s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:17<00:00,  3.39s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:17<00:00,  3.46s/it]", file = sys.stderr)
sleep(time_between_prints)
print("Saving model" +
      "\nSaving model current")
sleep(time_between_prints)
print("Updating state")
sleep(time_between_prints)
print("199 texts collected.")
sleep(time_between_prints)
print("Training on 8,768 character sequences.")
sleep(time_between_prints)
print("1/68 [..............................]")
sleep(time_between_prints)
print("- ETA: 19s - loss: 0.6057" +
      "\n2/68 [..............................]")
sleep(time_between_prints)
print("- ETA: 17s - loss: 0.5957" +
      "\n3/68 [>.............................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.6394" +
      "\n4/68 [>.............................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.6462" +
      "\n5/68 [=>............................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.6500" +
      "\n6/68 [=>............................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.6649" +
      "\n7/68 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.6532" +
      "\n8/68 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.6429" +
      "\n9/68 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.6345" +
      "\n10/68 [===>..........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.6312" +
      "\n11/68 [===>..........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.6284" +
      "\n12/68 [====>.........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.6290" +
      "\n13/68 [====>.........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.6402" +
      "\n14/68 [=====>........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.6281" +
      "\n15/68 [=====>........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.6214" +
      "\n16/68 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.6176" +
      "\n17/68 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.6213" +
      "\n18/68 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.6181" +
      "\n19/68 [=======>......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.6233" +
      "\n20/68 [=======>......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.6194" +
      "\n21/68 [========>.....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.6159" +
      "\n22/68 [========>.....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.6165" +
      "\n23/68 [=========>....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.6169" +
      "\n24/68 [=========>....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.6097" +
      "\n25/68 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.6085" +
      "\n26/68 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.6079" +
      "\n27/68 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.6063" +
      "\n28/68 [===========>..................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.6116" +
      "\n29/68 [===========>..................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.6123" +
      "\n30/68 [============>.................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.6132" +
      "\n31/68 [============>.................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.6154" +
      "\n32/68 [=============>................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.6108" +
      "\n33/68 [=============>................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.6123" +
      "\n34/68 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.6132" +
      "\n35/68 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.6158" +
      "\n36/68 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.6180" +
      "\n37/68 [===============>..............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.6183" +
      "\n38/68 [===============>..............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.6201" +
      "\n39/68 [================>.............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.6203" +
      "\n40/68 [================>.............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.6183" +
      "\n41/68 [=================>............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.6164" +
      "\n42/68 [=================>............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.6145" +
      "\n43/68 [=================>............]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.6151" +
      "\n44/68 [==================>...........]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.6161" +
      "\n45/68 [==================>...........]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.6200" +
      "\n46/68 [===================>..........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.6207" +
      "\n47/68 [===================>..........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.6154" +
      "\n48/68 [====================>.........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.6174" +
      "\n49/68 [====================>.........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.6199" +
      "\n50/68 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.6184" +
      "\n51/68 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.6141" +
      "\n52/68 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.6135" +
      "\n53/68 [======================>.......]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.6160" +
      "\n54/68 [======================>.......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.6201" +
      "\n55/68 [=======================>......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.6218" +
      "\n56/68 [=======================>......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.6231" +
      "\n57/68 [========================>.....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.6251" +
      "\n58/68 [========================>.....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.6284" +
      "\n59/68 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.6286" +
      "\n60/68 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.6317" +
      "\n61/68 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.6327" +
      "\n62/68 [==========================>...]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.6295" +
      "\n63/68 [==========================>...]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.6275" +
      "\n64/68 [===========================>..]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.6271" +
      "\n65/68 [===========================>..]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.6256" +
      "\n66/68 [============================>.]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.6250" +
      "\n67/68 [============================>.]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.6241" +
      "\n68/68 [==============================]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.6271" +
      "\n68/68 [==============================]")
sleep(time_between_prints)
print("- 21s 303ms/step - loss: 0.6271 - val_loss: 0.6678")
sleep(time_between_prints)
print("####################" +
      "\nTemperature: 0.2" +
      "\n####################")
sleep(time_between_prints)
print(
    "Nissin,Cup Noodles Spicy Seafood Flavour Instant Non-Fried Spicy Seafood Flavor,Pack,South Korea,5,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Spicy Seafood Flavor,Pack,South Korea,3.75,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Spicy Seafood Flavor,Pack,South Korea,4.5," +
      "\n" +
      "\n####################" +
      "\nTemperature: 0.5" +
      "\n####################")
sleep(time_between_prints)
print("Myojjing Ramen,Pack,South Korea,4.75,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Seafood Flavour,Cup,South Korea,4.75,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Very Veggie Sour Instant Non-Fried Noodles,Pack,South Korea,5," +
      "\n" +
      "\n####################" +
      "\nTemperature: 1.0" +
      "\n####################")
sleep(time_between_prints)
print("Nissin,Bowl,Japanea,4.5,")
sleep(time_between_prints)
print("Kura,Cup,Instant Noodles,Cup,China,5,")
sleep(time_between_prints)
print("Not,Childi,Mattick,South,South Korea,5,")
sleep(time_between_prints)
print("Generating text to output file.")
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:04<00:18,  4.54s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:08<00:12,  4.14s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:13<00:09,  4.53s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:16<00:04,  4.14s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:20<00:00,  4.07s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:20<00:00,  4.18s/it]", file = sys.stderr)
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:04<00:16,  4.05s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:08<00:12,  4.27s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:15<00:10,  5.30s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:21<00:05,  5.67s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:27<00:00,  6.03s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:27<00:00,  5.58s/it]", file = sys.stderr)
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:02<00:10,  2.72s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:06<00:09,  3.17s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:09<00:06,  3.10s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:11<00:02,  2.81s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:13<00:00,  2.48s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:13<00:00,  2.70s/it]", file = sys.stderr)
sleep(time_between_prints)
print("Saving model" +
      "\nSaving model current")
sleep(time_between_prints)
print("Saving model current")
sleep(time_between_prints)
print("Updating state")
sleep(time_between_prints)
print("199 texts collected.")
sleep(time_between_prints)
print("Training on 8,786 character sequences.")
sleep(time_between_prints)
print("1/68 [..............................]")
sleep(time_between_prints)
print("- ETA: 18s - loss: 0.5828" +
      "\n2/68 [..............................]")
sleep(time_between_prints)
print("- ETA: 18s - loss: 0.5123" +
      "\n3/68 [>.............................]")
sleep(time_between_prints)
print("- ETA: 18s - loss: 0.4945" +
      "\n4/68 [>.............................]")
sleep(time_between_prints)
print("- ETA: 18s - loss: 0.5086" +
      "\n5/68 [=>............................]")
sleep(time_between_prints)
print("- ETA: 17s - loss: 0.5224" +
      "\n6/68 [=>............................]")
sleep(time_between_prints)
print("- ETA: 18s - loss: 0.5561" +
      "\n7/68 [==>...........................] - ETA: 17s - loss: 0.5727" +
      "\n8/68 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 17s - loss: 0.5671" +
      "\n9/68 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.5804" +
      "\n10/68 [===>..........................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.5755" +
      "\n11/68 [===>..........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.5838" +
      "\n12/68 [====>.........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.5847" +
      "\n13/68 [====>.........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.5740" +
      "\n14/68 [=====>........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.5716" +
      "\n15/68 [=====>........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.5771" +
      "\n16/68 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.5721" +
      "\n17/68 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.5704" +
      "\n18/68 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.5744" +
      "\n19/68 [=======>......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.5699" +
      "\n20/68 [=======>......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.5840" +
      "\n21/68 [========>.....................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.5733" +
      "\n22/68 [========>.....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.5776" +
      "\n23/68 [=========>....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.5779" +
      "\n24/68 [=========>....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.5735" +
      "\n25/68 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.5780" +
      "\n26/68 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.5862" +
      "\n27/68 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.5864" +
      "\n28/68 [===========>..................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.5862" +
      "\n29/68 [===========>..................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.5839" +
      "\n30/68 [============>.................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.5822" +
      "\n31/68 [============>.................] - ETA: 10s - loss: 0.5874" +
      "\n32/68 [=============>................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.5888" +
      "\n33/68 [=============>................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.5855" +
      "\n34/68 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.5844" +
      "\n35/68 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.5839" +
      "\n36/68 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.5861" +
      "\n37/68 [===============>..............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.5902" +
      "\n38/68 [===============>..............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.5892" +
      "\n39/68 [================>.............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.5904" +
      "\n40/68 [================>.............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.5930" +
      "\n41/68 [=================>............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.5952" +
      "\n42/68 [=================>............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.5930" +
      "\n43/68 [=================>............]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.5915" +
      "\n44/68 [==================>...........]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.5934" +
      "\n45/68 [==================>...........]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.5932" +
      "\n46/68 [===================>..........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.5909" +
      "\n47/68 [===================>..........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.5930" +
      "\n48/68 [====================>.........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.5894" +
      "\n49/68 [====================>.........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.5906" +
      "\n50/68 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.5920" +
      "\n51/68 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.5905" +
      "\n52/68 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.5897" +
      "\n53/68 [======================>.......] - ETA: 4s - loss: 0.5871" +
      "\n54/68 [======================>.......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.5883" +
      "\n55/68 [=======================>......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.5883" +
      "\n56/68 [=======================>......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.5887" +
      "\n57/68 [========================>.....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.5925" +
      "\n58/68 [========================>.....] - ETA: 2s - loss: 0.5940" +
      "\n59/68 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.5960" +
      "\n60/68 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.5975" +
      "\n61/68 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.5955" +
      "\n62/68 [==========================>...]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.5946" +
      "\n63/68 [==========================>...]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.5942" +
      "\n64/68 [===========================>..]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.5959" +
      "\n65/68 [===========================>..]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.5982" +
      "\n66/68 [============================>.]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.5979" +
      "\n67/68 [============================>.]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.5971" +
      "\n68/68 [==============================]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.5992" +
      "\n68/68 [==============================]")
sleep(time_between_prints)
print("- 21s 312ms/step - loss: 0.5992 - val_loss: 0.6633")
sleep(time_between_prints)
print("####################" +
      "\nTemperature: 0.2" +
      "\n####################")
sleep(time_between_prints)
print("Nissin,Cup Noodles Beef Flavor Instant Noodles,Bowl,Taiwan,5,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Beef Flavor Instant Noodles,Bowl,Taway=TTL,Geaaffu,Bowl,Japan,3.5,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Beef Flavor Instant Noodles,Pack,Taa," +
      "\n" +
      "\n####################" +
      "\nTemperature: 0.5" +
      "\n####################")
sleep(time_between_prints)
print("Nissin,Cup Noodles Chicket Fujiwarate Flavor,Pack,Taiwan,4,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Chicken Flavor Instant Noodle,Bowl,Hong Kong,5,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Beef Flavour Instant Noodles,Pack,Hong Kong,3.75," +
      "\n" +
      "\n####################" +
      "\nTemperature: 1.0" +
      "\n####################")
sleep(time_between_prints)
print("Ogama Spicy,The Red Orientan,Bowling Spicy,Pack,Taiwan,5,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Prawn Fresh Ramen Nooda,Vellia,5,")
sleep(time_between_prints)
print("Samyang Foods,Hour Pot Chicketen Lempury,Udon,USA,5,")
sleep(time_between_prints)
print("Generating text to output file.")
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:03<00:14,  3.53s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:08<00:13,  4.49s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:10<00:06,  3.08s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:14<00:03,  3.46s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:17<00:00,  3.45s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:17<00:00,  3.52s/it]", file = sys.stderr)
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:04<00:16,  4.21s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:07<00:11,  3.80s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:12<00:08,  4.33s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:18<00:04,  4.93s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:21<00:00,  4.17s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:21<00:00,  4.27s/it]", file = sys.stderr)
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:04<00:18,  4.52s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:06<00:08,  2.84s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:09<00:05,  2.97s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:16<00:04,  4.54s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:20<00:00,  4.46s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:20<00:00,  4.11s/it]", file = sys.stderr)
sleep(time_between_prints)
print("Saving model" +
      "\nSaving model current")
sleep(time_between_prints)
print("Updating state")
sleep(time_between_prints)
print("199 texts collected.")
sleep(time_between_prints)
print("Training on 8,799 character sequences.")
sleep(time_between_prints)
print("1/68 [..............................]")
sleep(time_between_prints)
print("- ETA: 19s - loss: 0.5386" +
      "\n2/68 [..............................]")
sleep(time_between_prints)
print("- ETA: 17s - loss: 0.6574" +
      "\n3/68 [>.............................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.5975" +
      "\n4/68 [>.............................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.5944" +
      "\n5/68 [=>............................]")
sleep(time_between_prints)
print("- ETA: 16s - loss: 0.6044" +
      "\n6/68 [=>............................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.5864" +
      "\n7/68 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.5648" +
      "\n8/68 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.5828" +
      "\n9/68 [==>...........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.5882" +
      "\n10/68 [===>..........................]")
sleep(time_between_prints)
print("- ETA: 15s - loss: 0.5965" +
      "\n11/68 [===>..........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.6101" +
      "\n12/68 [====>.........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.6099" +
      "\n13/68 [====>.........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.6011" +
      "\n14/68 [=====>........................]")
sleep(time_between_prints)
print("- ETA: 14s - loss: 0.6008" +
      "\n15/68 [=====>........................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.6022" +
      "\n16/68 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.5981" +
      "\n17/68 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.6007" +
      "\n18/68 [======>.......................]")
sleep(time_between_prints)
print("- ETA: 13s - loss: 0.5958" +
      "\n19/68 [=======>......................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.5972" +
      "\n20/68 [=======>......................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.5911" +
      "\n21/68 [========>.....................]")
sleep(time_between_prints)
print("- ETA: 12s - loss: 0.5941" +
      "\n22/68 [========>.....................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.5933" +
      "\n23/68 [=========>....................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.5943" +
      "\n24/68 [=========>....................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.6017" +
      "\n25/68 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 11s - loss: 0.5980" +
      "\n26/68 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.5975" +
      "\n27/68 [==========>...................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.5991" +
      "\n28/68 [===========>..................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.6008" +
      "\n29/68 [===========>..................]")
sleep(time_between_prints)
print("- ETA: 10s - loss: 0.5976" +
      "\n30/68 [============>.................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.5935" +
      "\n31/68 [============>.................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.5882" +
      "\n32/68 [=============>................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.5907" +
      "\n33/68 [=============>................]")
sleep(time_between_prints)
print("- ETA: 9s - loss: 0.5897" +
      "\n34/68 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.5905" +
      "\n35/68 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.5939" +
      "\n36/68 [==============>...............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.5900" +
      "\n37/68 [===============>..............]")
sleep(time_between_prints)
print("- ETA: 8s - loss: 0.5904" +
      "\n38/68 [===============>..............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.5940" +
      "\n39/68 [================>.............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.5916" +
      "\n40/68 [================>.............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.5885" +
      "\n41/68 [=================>............]")
sleep(time_between_prints)
print("- ETA: 7s - loss: 0.5862" +
      "\n42/68 [=================>............]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.5892" +
      "\n43/68 [=================>............]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.5905" +
      "\n44/68 [==================>...........]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.5891" +
      "\n45/68 [==================>...........]")
sleep(time_between_prints)
print("- ETA: 6s - loss: 0.5868" +
      "\n46/68 [===================>..........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.5878" +
      "\n47/68 [===================>..........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.5931" +
      "\n48/68 [====================>.........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.5950" +
      "\n49/68 [====================>.........]")
sleep(time_between_prints)
print("- ETA: 5s - loss: 0.5940" +
      "\n50/68 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.5937" +
      "\n51/68 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.5908" +
      "\n52/68 [=====================>........]")
sleep(time_between_prints)
print("- ETA: 4s - loss: 0.5910" +
      "\n53/68 [======================>.......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.5914" +
      "\n54/68 [======================>.......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.5899" +
      "\n55/68 [=======================>......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.5917" +
      "\n56/68 [=======================>......]")
sleep(time_between_prints)
print("- ETA: 3s - loss: 0.5918" +
      "\n57/68 [========================>.....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.5920" +
      "\n58/68 [========================>.....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.5902" +
      "\n59/68 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.5882" +
      "\n60/68 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 2s - loss: 0.5880" +
      "\n61/68 [=========================>....]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.5864" +
      "\n62/68 [==========================>...]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.5887" +
      "\n63/68 [==========================>...]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.5898" +
      "\n64/68 [===========================>..]")
sleep(time_between_prints)
print("- ETA: 1s - loss: 0.5905" +
      "\n65/68 [===========================>..]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.5887" +
      "\n66/68 [============================>.]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.5894" +
      "\n67/68 [============================>.]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.5903" +
      "\n68/68 [==============================]")
sleep(time_between_prints)
print("- ETA: 0s - loss: 0.5917" +
      "\n68/68 [==============================]")
sleep(time_between_prints)
print("- 20s 301ms/step - loss: 0.5917 - val_loss: 0.5836")
sleep(time_between_prints)
print("####################" +
      "\nTemperature: 0.2" +
      "\n####################")
sleep(time_between_prints)
print("Nissin,Cup Noodles Beef Flavor Instant Non-Fried Noodles,Pack,Singapore,5,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Spicy Seafood Flavor Instant Noodles,Pack,USA,3.75,")
sleep(time_between_prints)
print("Samyang Foods,Sari Ramen Noodle Soup (More Saich,Cup,USA,3.75," +
      "\n" +
      "\n####################" +
      "\nTemperature: 0.5" +
      "\n####################")
sleep(time_between_prints)
print("Nissin,Cup Noodles Beef Flavor Ramen Noodle Curry,Pack,USA,3.75,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Botten Noodle Soup (Men),Cup,USA,3.75,")
sleep(time_between_prints)
print("Nissin,Cup Noodles Spicy Hot Goreng Chicken Flavor Instant Noodles,Pack,USA,5," +
      "\n" +
      "\n####################" +
      "\nTemperature: 1.0" +
      "\n####################")
sleep(time_between_prints)
print("Muru Soup Included Song Throason Crack,Mast Noodle,Pack,Singapore,5,")
sleep(time_between_prints)
print("Nissin,Germy Sweet Gahomis Snack Flavor,Pack,China,4.75,")
sleep(time_between_prints)
print("Nissin,Cup Noodle Men Weia Caha Rice Noodles,Pack,Germany,3.75,")
sleep(time_between_prints)
print("Generating text to output file.")
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:03<00:14,  3.58s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:07<00:11,  3.78s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:11<00:07,  3.90s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:15<00:03,  3.91s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:20<00:00,  4.27s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:20<00:00,  4.08s/it]", file = sys.stderr)
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:05<00:20,  5.23s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:08<00:12,  4.19s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:10<00:06,  3.00s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:15<00:03,  3.90s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:19<00:00,  3.98s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:19<00:00,  3.94s/it]", file = sys.stderr)
sleep(time_between_prints)
print("0%|          | 0/5 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 1/5 [00:02<00:10,  2.63s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 2/5 [00:06<00:10,  3.55s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 3/5 [00:14<00:10,  5.29s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 4/5 [00:16<00:04,  4.13s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:20<00:00,  4.10s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 5/5 [00:20<00:00,  4.12s/it]", file = sys.stderr)
sleep(time_between_prints)
print("Saving model" +
      "\nSaving model current")
sleep(time_between_prints)
print("Saving model current")
sleep(time_between_prints)
print("Updating state" +
      "\nGenerating final text")
sleep(time_between_prints)
print("0%|          | 0/50 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("2%|▏         | 1/50 [00:03<02:31,  3.09s/it]", file = sys.stderr)
sleep(time_between_prints)
print("4%|▍         | 2/50 [00:06<02:23,  2.99s/it]", file = sys.stderr)
sleep(time_between_prints)
print("6%|▌         | 3/50 [00:09<02:27,  3.14s/it]", file = sys.stderr)
sleep(time_between_prints)
print("8%|▊         | 4/50 [00:13<02:43,  3.56s/it]", file = sys.stderr)
sleep(time_between_prints)
print("10%|█         | 5/50 [00:17<02:50,  3.79s/it]", file = sys.stderr)
sleep(time_between_prints)
print("12%|█▏        | 6/50 [00:21<02:40,  3.66s/it]", file = sys.stderr)
sleep(time_between_prints)
print("14%|█▍        | 7/50 [00:24<02:36,  3.63s/it]", file = sys.stderr)
sleep(time_between_prints)
print("16%|█▌        | 8/50 [00:28<02:30,  3.59s/it]", file = sys.stderr)
sleep(time_between_prints)
print("18%|█▊        | 9/50 [00:31<02:20,  3.43s/it]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 10/50 [00:35<02:22,  3.57s/it]", file = sys.stderr)
sleep(time_between_prints)
print("22%|██▏       | 11/50 [00:37<02:04,  3.19s/it]", file = sys.stderr)
sleep(time_between_prints)
print("24%|██▍       | 12/50 [00:41<02:12,  3.49s/it]", file = sys.stderr)
sleep(time_between_prints)
print("26%|██▌       | 13/50 [00:46<02:22,  3.86s/it]", file = sys.stderr)
sleep(time_between_prints)
print("28%|██▊       | 14/50 [00:50<02:25,  4.05s/it]", file = sys.stderr)
sleep(time_between_prints)
print("30%|███       | 15/50 [00:54<02:17,  3.94s/it]", file = sys.stderr)
sleep(time_between_prints)
print("32%|███▏      | 16/50 [00:57<01:59,  3.50s/it]", file = sys.stderr)
sleep(time_between_prints)
print("34%|███▍      | 17/50 [01:00<01:55,  3.49s/it]", file = sys.stderr)
sleep(time_between_prints)
print("36%|███▌      | 18/50 [01:03<01:48,  3.38s/it]", file = sys.stderr)
sleep(time_between_prints)
print("38%|███▊      | 19/50 [01:07<01:50,  3.56s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 20/50 [01:10<01:42,  3.43s/it]", file = sys.stderr)
sleep(time_between_prints)
print("42%|████▏     | 21/50 [01:13<01:37,  3.35s/it]", file = sys.stderr)
sleep(time_between_prints)
print("44%|████▍     | 22/50 [01:17<01:35,  3.40s/it]", file = sys.stderr)
sleep(time_between_prints)
print("46%|████▌     | 23/50 [01:20<01:30,  3.33s/it]", file = sys.stderr)
sleep(time_between_prints)
print("48%|████▊     | 24/50 [01:24<01:28,  3.39s/it]", file = sys.stderr)
sleep(time_between_prints)
print("50%|█████     | 25/50 [01:27<01:24,  3.40s/it]", file = sys.stderr)
sleep(time_between_prints)
print("52%|█████▏    | 26/50 [01:30<01:19,  3.32s/it]", file = sys.stderr)
sleep(time_between_prints)
print("54%|█████▍    | 27/50 [01:32<01:08,  2.96s/it]", file = sys.stderr)
sleep(time_between_prints)
print("56%|█████▌    | 28/50 [01:36<01:07,  3.05s/it]", file = sys.stderr)
sleep(time_between_prints)
print("58%|█████▊    | 29/50 [01:40<01:12,  3.47s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 30/50 [01:43<01:08,  3.44s/it]", file = sys.stderr)
sleep(time_between_prints)
print("62%|██████▏   | 31/50 [01:46<00:58,  3.06s/it]", file = sys.stderr)
sleep(time_between_prints)
print("64%|██████▍   | 32/50 [01:50<01:00,  3.37s/it]", file = sys.stderr)
sleep(time_between_prints)
print("66%|██████▌   | 33/50 [01:53<00:56,  3.31s/it]", file = sys.stderr)
sleep(time_between_prints)
print("68%|██████▊   | 34/50 [01:55<00:49,  3.08s/it]", file = sys.stderr)
sleep(time_between_prints)
print("70%|███████   | 35/50 [01:57<00:40,  2.69s/it]", file = sys.stderr)
sleep(time_between_prints)
print("72%|███████▏  | 36/50 [02:01<00:40,  2.92s/it]", file = sys.stderr)
sleep(time_between_prints)
print("74%|███████▍  | 37/50 [02:05<00:43,  3.33s/it]", file = sys.stderr)
sleep(time_between_prints)
print("76%|███████▌  | 38/50 [02:09<00:41,  3.50s/it]", file = sys.stderr)
sleep(time_between_prints)
print("78%|███████▊  | 39/50 [02:12<00:36,  3.28s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 40/50 [02:16<00:35,  3.52s/it]", file = sys.stderr)
sleep(time_between_prints)
print("82%|████████▏ | 41/50 [02:20<00:33,  3.70s/it]", file = sys.stderr)
sleep(time_between_prints)
print("84%|████████▍ | 42/50 [02:24<00:31,  3.98s/it]", file = sys.stderr)
sleep(time_between_prints)
print("86%|████████▌ | 43/50 [02:26<00:23,  3.35s/it]", file = sys.stderr)
sleep(time_between_prints)
print("88%|████████▊ | 44/50 [02:29<00:19,  3.19s/it]", file = sys.stderr)
sleep(time_between_prints)
print("90%|█████████ | 45/50 [02:34<00:18,  3.63s/it]", file = sys.stderr)
sleep(time_between_prints)
print("92%|█████████▏| 46/50 [02:37<00:14,  3.50s/it]", file = sys.stderr)
sleep(time_between_prints)
print("94%|█████████▍| 47/50 [02:40<00:09,  3.32s/it]", file = sys.stderr)
sleep(time_between_prints)
print("96%|█████████▌| 48/50 [02:43<00:06,  3.31s/it]", file = sys.stderr)
sleep(time_between_prints)
print("98%|█████████▊| 49/50 [02:47<00:03,  3.58s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 50/50 [02:52<00:00,  3.96s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 50/50 [02:52<00:00,  3.45s/it]", file = sys.stderr)
sleep(time_between_prints)
print("0%|          | 0/50 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("2%|▏         | 1/50 [00:04<03:37,  4.45s/it]", file = sys.stderr)
sleep(time_between_prints)
print("4%|▍         | 2/50 [00:07<03:02,  3.81s/it]", file = sys.stderr)
sleep(time_between_prints)
print("6%|▌         | 3/50 [00:11<03:05,  3.94s/it]", file = sys.stderr)
sleep(time_between_prints)
print("8%|▊         | 4/50 [00:14<02:27,  3.22s/it]", file = sys.stderr)
sleep(time_between_prints)
print("10%|█         | 5/50 [00:17<02:29,  3.33s/it]", file = sys.stderr)
sleep(time_between_prints)
print("12%|█▏        | 6/50 [00:20<02:23,  3.27s/it]", file = sys.stderr)
sleep(time_between_prints)
print("14%|█▍        | 7/50 [00:22<02:00,  2.80s/it]", file = sys.stderr)
sleep(time_between_prints)
print("16%|█▌        | 8/50 [00:25<01:53,  2.71s/it]", file = sys.stderr)
sleep(time_between_prints)
print("18%|█▊        | 9/50 [00:28<01:58,  2.89s/it]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 10/50 [00:31<02:01,  3.04s/it]", file = sys.stderr)
sleep(time_between_prints)
print("22%|██▏       | 11/50 [00:35<02:07,  3.26s/it]", file = sys.stderr)
sleep(time_between_prints)
print("24%|██▍       | 12/50 [00:40<02:24,  3.81s/it]", file = sys.stderr)
sleep(time_between_prints)
print("26%|██▌       | 13/50 [00:43<02:08,  3.49s/it]", file = sys.stderr)
sleep(time_between_prints)
print("28%|██▊       | 14/50 [00:48<02:20,  3.90s/it]", file = sys.stderr)
sleep(time_between_prints)
print("30%|███       | 15/50 [00:52<02:21,  4.05s/it]", file = sys.stderr)
sleep(time_between_prints)
print("32%|███▏      | 16/50 [00:53<01:50,  3.25s/it]", file = sys.stderr)
sleep(time_between_prints)
print("34%|███▍      | 17/50 [00:57<01:48,  3.30s/it]", file = sys.stderr)
sleep(time_between_prints)
print("36%|███▌      | 18/50 [01:01<01:50,  3.46s/it]", file = sys.stderr)
sleep(time_between_prints)
print("38%|███▊      | 19/50 [01:04<01:44,  3.38s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 20/50 [01:07<01:35,  3.18s/it]", file = sys.stderr)
sleep(time_between_prints)
print("42%|████▏     | 21/50 [01:11<01:41,  3.50s/it]", file = sys.stderr)
sleep(time_between_prints)
print("44%|████▍     | 22/50 [01:16<01:49,  3.90s/it]", file = sys.stderr)
sleep(time_between_prints)
print("46%|████▌     | 23/50 [01:18<01:30,  3.35s/it]", file = sys.stderr)
sleep(time_between_prints)
print("48%|████▊     | 24/50 [01:22<01:36,  3.72s/it]", file = sys.stderr)
sleep(time_between_prints)
print("50%|█████     | 25/50 [01:25<01:28,  3.54s/it]", file = sys.stderr)
sleep(time_between_prints)
print("52%|█████▏    | 26/50 [01:28<01:17,  3.25s/it]", file = sys.stderr)
sleep(time_between_prints)
print("54%|█████▍    | 27/50 [01:31<01:14,  3.22s/it]", file = sys.stderr)
sleep(time_between_prints)
print("56%|█████▌    | 28/50 [01:35<01:14,  3.39s/it]", file = sys.stderr)
sleep(time_between_prints)
print("58%|█████▊    | 29/50 [01:40<01:23,  3.97s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 30/50 [01:45<01:21,  4.08s/it]", file = sys.stderr)
sleep(time_between_prints)
print("62%|██████▏   | 31/50 [01:49<01:17,  4.08s/it]", file = sys.stderr)
sleep(time_between_prints)
print("64%|██████▍   | 32/50 [01:52<01:11,  3.96s/it]", file = sys.stderr)
sleep(time_between_prints)
print("66%|██████▌   | 33/50 [01:58<01:16,  4.48s/it]", file = sys.stderr)
sleep(time_between_prints)
print("68%|██████▊   | 34/50 [02:02<01:08,  4.29s/it]", file = sys.stderr)
sleep(time_between_prints)
print("70%|███████   | 35/50 [02:05<00:58,  3.90s/it]", file = sys.stderr)
sleep(time_between_prints)
print("72%|███████▏  | 36/50 [02:08<00:52,  3.75s/it]", file = sys.stderr)
sleep(time_between_prints)
print("74%|███████▍  | 37/50 [02:11<00:45,  3.48s/it]", file = sys.stderr)
sleep(time_between_prints)
print("76%|███████▌  | 38/50 [02:14<00:38,  3.20s/it]", file = sys.stderr)
sleep(time_between_prints)
print("78%|███████▊  | 39/50 [02:17<00:37,  3.37s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 40/50 [02:21<00:33,  3.32s/it]", file = sys.stderr)
sleep(time_between_prints)
print("82%|████████▏ | 41/50 [02:23<00:27,  3.07s/it]", file = sys.stderr)
sleep(time_between_prints)
print("84%|████████▍ | 42/50 [02:26<00:23,  2.97s/it]", file = sys.stderr)
sleep(time_between_prints)
print("86%|████████▌ | 43/50 [02:30<00:23,  3.36s/it]", file = sys.stderr)
sleep(time_between_prints)
print("88%|████████▊ | 44/50 [02:33<00:19,  3.19s/it]", file = sys.stderr)
sleep(time_between_prints)
print("90%|█████████ | 45/50 [02:35<00:14,  3.00s/it]", file = sys.stderr)
sleep(time_between_prints)
print("92%|█████████▏| 46/50 [02:40<00:13,  3.35s/it]", file = sys.stderr)
sleep(time_between_prints)
print("94%|█████████▍| 47/50 [02:42<00:09,  3.11s/it]", file = sys.stderr)
sleep(time_between_prints)
print("96%|█████████▌| 48/50 [02:44<00:05,  2.60s/it]", file = sys.stderr)
sleep(time_between_prints)
print("98%|█████████▊| 49/50 [02:48<00:03,  3.04s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 50/50 [02:49<00:00,  2.57s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 50/50 [02:49<00:00,  3.39s/it]", file = sys.stderr)
sleep(time_between_prints)
print("0%|          | 0/50 [00:00<?, ?it/s]", file = sys.stderr)
sleep(time_between_prints)
print("2%|▏         | 1/50 [00:02<01:52,  2.30s/it]", file = sys.stderr)
sleep(time_between_prints)
print("4%|▍         | 2/50 [00:08<03:44,  4.68s/it]", file = sys.stderr)
sleep(time_between_prints)
print("6%|▌         | 3/50 [00:12<03:32,  4.53s/it]", file = sys.stderr)
sleep(time_between_prints)
print("8%|▊         | 4/50 [00:22<04:57,  6.46s/it]", file = sys.stderr)
sleep(time_between_prints)
print("10%|█         | 5/50 [00:25<03:56,  5.25s/it]", file = sys.stderr)
sleep(time_between_prints)
print("12%|█▏        | 6/50 [00:32<04:17,  5.85s/it]", file = sys.stderr)
sleep(time_between_prints)
print("14%|█▍        | 7/50 [00:35<03:30,  4.91s/it]", file = sys.stderr)
sleep(time_between_prints)
print("16%|█▌        | 8/50 [00:38<02:59,  4.28s/it]", file = sys.stderr)
sleep(time_between_prints)
print("18%|█▊        | 9/50 [00:40<02:30,  3.67s/it]", file = sys.stderr)
sleep(time_between_prints)
print("20%|██        | 10/50 [00:44<02:29,  3.73s/it]", file = sys.stderr)
sleep(time_between_prints)
print("22%|██▏       | 11/50 [00:48<02:26,  3.75s/it]", file = sys.stderr)
sleep(time_between_prints)
print("24%|██▍       | 12/50 [00:52<02:29,  3.93s/it]", file = sys.stderr)
sleep(time_between_prints)
print("26%|██▌       | 13/50 [00:57<02:29,  4.03s/it]", file = sys.stderr)
sleep(time_between_prints)
print("28%|██▊       | 14/50 [01:03<02:54,  4.86s/it]", file = sys.stderr)
sleep(time_between_prints)
print("30%|███       | 15/50 [01:05<02:16,  3.90s/it]", file = sys.stderr)
sleep(time_between_prints)
print("32%|███▏      | 16/50 [01:10<02:22,  4.21s/it]", file = sys.stderr)
sleep(time_between_prints)
print("34%|███▍      | 17/50 [01:14<02:17,  4.17s/it]", file = sys.stderr)
sleep(time_between_prints)
print("36%|███▌      | 18/50 [01:18<02:15,  4.22s/it]", file = sys.stderr)
sleep(time_between_prints)
print("38%|███▊      | 19/50 [01:21<01:55,  3.73s/it]", file = sys.stderr)
sleep(time_between_prints)
print("40%|████      | 20/50 [01:24<01:45,  3.53s/it]", file = sys.stderr)
sleep(time_between_prints)
print("42%|████▏     | 21/50 [01:28<01:50,  3.79s/it]", file = sys.stderr)
sleep(time_between_prints)
print("44%|████▍     | 22/50 [01:30<01:30,  3.22s/it]", file = sys.stderr)
sleep(time_between_prints)
print("46%|████▌     | 23/50 [01:33<01:24,  3.13s/it]", file = sys.stderr)
sleep(time_between_prints)
print("48%|████▊     | 24/50 [01:35<01:09,  2.68s/it]", file = sys.stderr)
sleep(time_between_prints)
print("50%|█████     | 25/50 [01:40<01:27,  3.49s/it]", file = sys.stderr)
sleep(time_between_prints)
print("52%|█████▏    | 26/50 [01:44<01:23,  3.47s/it]", file = sys.stderr)
sleep(time_between_prints)
print("54%|█████▍    | 27/50 [01:47<01:22,  3.59s/it]", file = sys.stderr)
sleep(time_between_prints)
print("56%|█████▌    | 28/50 [01:50<01:10,  3.21s/it]", file = sys.stderr)
sleep(time_between_prints)
print("58%|█████▊    | 29/50 [01:54<01:13,  3.51s/it]", file = sys.stderr)
sleep(time_between_prints)
print("60%|██████    | 30/50 [01:59<01:16,  3.85s/it]", file = sys.stderr)
sleep(time_between_prints)
print("62%|██████▏   | 31/50 [02:02<01:08,  3.60s/it]", file = sys.stderr)
sleep(time_between_prints)
print("64%|██████▍   | 32/50 [02:06<01:09,  3.88s/it]", file = sys.stderr)
sleep(time_between_prints)
print("66%|██████▌   | 33/50 [02:09<00:58,  3.45s/it]", file = sys.stderr)
sleep(time_between_prints)
print("68%|██████▊   | 34/50 [02:13<00:58,  3.64s/it]", file = sys.stderr)
sleep(time_between_prints)
print("70%|███████   | 35/50 [02:18<01:03,  4.23s/it]", file = sys.stderr)
sleep(time_between_prints)
print("72%|███████▏  | 36/50 [02:23<01:01,  4.38s/it]", file = sys.stderr)
sleep(time_between_prints)
print("74%|███████▍  | 37/50 [02:25<00:48,  3.74s/it]", file = sys.stderr)
sleep(time_between_prints)
print("76%|███████▌  | 38/50 [02:30<00:48,  4.01s/it]", file = sys.stderr)
sleep(time_between_prints)
print("78%|███████▊  | 39/50 [02:34<00:45,  4.14s/it]", file = sys.stderr)
sleep(time_between_prints)
print("80%|████████  | 40/50 [02:38<00:39,  3.90s/it]", file = sys.stderr)
sleep(time_between_prints)
print("82%|████████▏ | 41/50 [02:41<00:34,  3.84s/it]", file = sys.stderr)
sleep(time_between_prints)
print("84%|████████▍ | 42/50 [02:45<00:30,  3.85s/it]", file = sys.stderr)
sleep(time_between_prints)
print("86%|████████▌ | 43/50 [02:50<00:29,  4.14s/it]", file = sys.stderr)
sleep(time_between_prints)
print("88%|████████▊ | 44/50 [02:54<00:24,  4.00s/it]", file = sys.stderr)
sleep(time_between_prints)
print("90%|█████████ | 45/50 [02:58<00:20,  4.01s/it]", file = sys.stderr)
sleep(time_between_prints)
print("92%|█████████▏| 46/50 [03:01<00:14,  3.66s/it]", file = sys.stderr)
sleep(time_between_prints)
print("94%|█████████▍| 47/50 [03:05<00:11,  3.94s/it]", file = sys.stderr)
sleep(time_between_prints)
print("96%|█████████▌| 48/50 [03:12<00:09,  4.84s/it]", file = sys.stderr)
sleep(time_between_prints)
print("98%|█████████▊| 49/50 [03:16<00:04,  4.37s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 50/50 [03:18<00:00,  3.88s/it]", file = sys.stderr)
sleep(time_between_prints)
print("100%|██████████| 50/50 [03:18<00:00,  3.97s/it]", file = sys.stderr)
sleep(time_between_prints)
print("Saving final model")
sleep(time_between_prints)
print("Updating state")
sleep(time_between_prints)
print("------------------------------------")
sleep(time_between_prints)
