import { FC, useEffect } from "react";
import axios from 'axios';
import { Card } from "@nextui-org/react";

//testing purposes
async function delayedString(str: string) {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(str);
      }, 6000);
    });
  }

export interface ChatMessageProps {
    direction: 'right' | 'left';
    agentName: 'math' | 'story';
    query: string;
}

export const ChatMessage: FC<ChatMessageProps> = ({
    direction,
    agentName,
    query
}) => {
    useEffect(() => {

    }, [])

    return <div className={`p-3 w-full flex flex-row${direction == 'left' ? '' : '-reverse'} h-[15vh]`}>
        <Card className='w-full'>
          
        </Card>
    </div>
}