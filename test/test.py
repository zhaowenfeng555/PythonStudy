import paddlehub as hub
model = hub.Module(name='ernie_tiny', version='2.0.1', task='seq-cls', num_classes=2)

train_dataset = hub.datasets.ChnSentiCorp(
    tokenizer=model.get_tokenizer(), max_seq_len=128, mode='train')
dev_dataset = hub.datasets.ChnSentiCorp(
    tokenizer=model.get_tokenizer(), max_seq_len=128, mode='dev')

import paddle

optimizer = paddle.optimizer.Adam(learning_rate=5e-5, parameters=model.parameters())
trainer = hub.Trainer(model, optimizer, checkpoint_dir='test_ernie_text_cls', use_gpu=False)

trainer.train(train_dataset, epochs=3, batch_size=32, eval_dataset=dev_dataset, save_interval=1)
