import { FC, useEffect, useState } from "react";
import axios from 'axios';
import { Card, CardBody } from "@nextui-org/react";
import { AgentMapping } from "@/exports";

import { User, User2 } from "lucide-react";
import { TypeAnimation } from 'react-type-animation';
import type { } from 'ldrs'

//testing purposes
async function delayedString(str: string): Promise<string> {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(str);
        }, 6000);
    });
}

const _ = async (s: string) => {
    const r = await delayedString(s);
    return r;
}

export interface ChatMessageProps {
    direction: 'right' | 'left';
    agentName: 'math' | 'story' | 'user';
    query: string;
}

export interface ChatBreakProps {
    size: number
}

export const ChatBreak: FC<ChatBreakProps> = ({
    size
}) => {
    return <div className={`w-full h-[${size}px]`} />
}

export function isChatMessageProps(item: ChatBreakProps | ChatMessageProps): item is ChatMessageProps {
    return 'direction' in item && 'agentName' in item && 'query' in item;
}

export function isChatBreakProps(item: ChatBreakProps | ChatMessageProps): item is ChatBreakProps {
    return 'size' in item;
}

export const ChatMessage: FC<ChatMessageProps> = ({
    direction,
    agentName,
    query
}) => {
    const [response, setResponse] = useState('');

    useEffect(() => {
        const _ = async (s: string, v: string) => {
            const r = await delayedString(s);
            setResponse(r);
        }

        if (agentName != 'user')
            _(query, agentName)
    }, [])


    return <div className={`p-0 w-full flex justify-start flex-row${direction == 'left' ? '' : '-reverse'} h-[15vh]`}>
        <Card className='w-[41%] h-full p-2'>
            {agentName != 'user' && <CardBody className='p-2 flex flex-col gap-y-2'>
                <div className='flex flex-row gap-x-3 items-center'>
                    {AgentMapping[agentName].icon}

                    <p className='text-2xl font-semibold'>{AgentMapping[agentName].displayName}</p>
                </div>
                <div className='flex items-center justify-center' style={{
                    alignItems: response == '' ? 'center' : 'center',
                    justifyContent: response == '' ? 'center' : 'start',
                }}>

                    {response != '' ? <TypeAnimation
                        sequence={[response]}
                        wrapper="span"
                        speed={50}
                        style={{ fontSize: '1.125rem', lineHeight: '1.75rem', display: 'inline-block'}}
                        repeat={0}
                        cursor={false}
                    /> :
                        <l-hatch
                            size="28"
                            stroke="4"
                            speed="3.5"
                            color={AgentMapping[agentName].color}
                        ></l-hatch>}
                </div>
            </CardBody>}
            {agentName == 'user' && <CardBody className='p-2 flex flex-col gap-y-2'>
                <div className='flex flex-row gap-x-3 items-center'>
                    <User2 color={'blue'} />
                    <p className='text-2xl font-semibold'>User</p>
                </div>
                <p className='text-base'>{query}</p>
            </CardBody>}
        </Card>
    </div>
}