import { FC, useEffect } from "react";
import axios from 'axios';

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

    return <div className='w-full'>
        
    </div>
}