import os
from transformers import GPT2LMHeadModel, GPT2TokenizerFast, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

# Modelo base en español (puedes cambiarlo por PlanTL-GOB-ES/gpt2-base-spanish o mrm8488/spanish-gpt2)
model_name = "mrm8488/spanish-gpt2"

# Cargar tokenizador y modelo base
tokenizer = GPT2TokenizerFast.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def load_dataset(train_file, tokenizer, block_size=128):
    return TextDataset(
        tokenizer=tokenizer,
        file_path=train_file,
        block_size=block_size,
        overwrite_cache=True,
    )

# Asegúrate de tener el corpus.txt en la raíz
train_file = "corpus.txt"
dataset = load_dataset(train_file, tokenizer)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

training_args = TrainingArguments(
    output_dir="./finetuned-model",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=500,
    save_total_limit=2,
    logging_steps=100,
    learning_rate=5e-5,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

trainer.train()
trainer.save_model("./finetuned-model")
tokenizer.save_pretrained("./finetuned-model")
