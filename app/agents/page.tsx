"use client";

import Image from 'next/image'
import { IdeaCard } from '@/components/agents/IdeaCard';
import { useRef, useState } from 'react';
import useAutosizeTextArea from '@/hooks/useAutosizeTextArea';
import { Textarea, Button } from '@nextui-org/react';
import { SearchCode } from 'lucide-react';

import { Mention, MentionsInput } from 'react-mentions'

import defaultStyle from './defaultStyle'
import defaultMentionStyle from './defaultMentionStyle';

import './s.css'
import Container from '@/components/agents/Container';

const agents = [
    {
        id: 'math',
        display: 'Math Agent'
    },
    {
        id: 'story',
        display: 'Story Agent'
    },
]

export default function AgentsPage() {
    const [value, setValue] = useState('');
    const textAreaRef = useRef<HTMLTextAreaElement>(null);
    const [chatStarted, setChatStarted] = useState(false);

    useAutosizeTextArea(textAreaRef.current, value);

    const handleQuery = () => {
        setChatStarted(true);
        setValue('')
    }

    return (
        <main className="w-full h-screen overflow-hidden flex flex-row">
            <div className="h-full w-1/6"></div>
            <div className="h-full w-5/6 bg-white relative">
                {!chatStarted ? (<div className='center-panel flex flex-col w-2/3 absolute top-[40%] left-1/2 transform -translate-x-1/2 -translate-y-1/2 items-center justify-center gap-y-8'>
                    <Image src={'https://avatars.githubusercontent.com/u/130198651?v=4'} width={460} height={460} alt={'AGI Research Logo'} className='w-[10%] aspect-square rounded-full' />
                    <div className='flex flex-row justify-between w-full gap-x-3 pt-4'>
                        <IdeaCard />
                        <IdeaCard />
                        <IdeaCard />
                        <IdeaCard />
                    </div>
                </div>) : (<Container>
                    <div>

                    </div>
                </Container>)}
                <div className='input-panel flex w-2/3 absolute left-0 right-0 mx-auto bottom-[20px] bg-[#F4F4F4] h-fit overflow-visible outline-none flex-row p-4 rounded-2xl gap-x-4 items-center'>
                    <MentionsInput
                        value={value}
                        onChange={(e) => setValue(e.target.value)}
                        style={defaultStyle}
                        className={'mention_input'}
                        placeholder={"Mention people using '@'"}
                        a11ySuggestionsListLabel={"Suggested mentions"}
                        allowSuggestionsAboveCursor={true}
                        customSuggestionsContainer={(children) => <div><span style={{ fontWeight: "bold" }}><h2>This container has customised suggestions</h2></span>{children}</div>}
                    >
                        <Mention data={agents} onAdd={undefined} style={defaultMentionStyle} trigger={'@'} />
                    </MentionsInput>
                    <Button isIconOnly className='bg-transparent hover:opacity-40' onClick={() => handleQuery()}>
                        <SearchCode />
                    </Button>

                </div>
            </div>
        </main>
    );
}



