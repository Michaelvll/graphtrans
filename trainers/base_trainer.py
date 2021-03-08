from tqdm import tqdm
import torch

class BaseTrainer:
    @staticmethod
    def transform(args):
        return None

    @staticmethod
    def add_args(parser):
        pass
    
    @staticmethod
    def train(model, device, loader, optimizer, args, calc_loss):
        model.train()

        loss_accum = 0
        for step, batch in enumerate(tqdm(loader, desc="Train")):
            batch = batch.to(device)

            if batch.x.shape[0] == 1 or batch.batch[-1] == 0:
                pass
            else:
                optimizer.zero_grad()
                pred_list = model(batch)
                
                loss = calc_loss(pred_list, batch)

                loss.backward()
                if args.grad_clip is not None:
                    torch.nn.utils.clip_grad_norm_(model.parameters(), args.grad_clip)
                optimizer.step()

                loss_accum += loss.item()

        print('Average training loss: {}'.format(loss_accum / (step + 1)))
        return loss_accum / (step + 1)

    @staticmethod
    def name(args):
        raise NotImplemented
