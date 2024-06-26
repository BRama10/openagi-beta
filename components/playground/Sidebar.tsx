import React from 'react';

export default () => {
    const onDragStart = (event: any, nodeType: any) => {
      event.dataTransfer.setData('application/reactflow', nodeType);
      event.dataTransfer.effectAllowed = 'move';
    };
  
    return (
      <aside className='w-full h-full flex flex-col p-4'>
        <div className="text-white text-4xl w-full text-center">Editor</div>
        <div className="dndnode input" onDragStart={(event) => onDragStart(event, 'input')} draggable>
          Input Node
        </div>
        <div className="dndnode" onDragStart={(event) => onDragStart(event, 'default')} draggable>
          Default Node
        </div>
        <div className="dndnode output" onDragStart={(event) => onDragStart(event, 'output')} draggable>
          Output Node
        </div>
      </aside>
    );
  };